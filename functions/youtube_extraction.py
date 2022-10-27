from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.cloud import storage

import pandas as pd

# Setup YT API Credentials and Args
DEVELOPER_KEY = "AIzaSyB-l0tlFDOWByuB0_3OWKtQNnUh_hq58Jo"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# Initialize variables
videos = []
channels = []
options = {
    'query': 'CSGO Tips', ## Default
    'max_results': 50
}
BUCKET_NAME = 'buffme'
FILE_PATH = 'data/videos.csv'


def extract_videos(request):
    ## Get request query data
    content_type = request.headers['content-type']
    if content_type == 'application/json':
        request_json = request.get_json(silent=True)
        if request_json and 'query' in request_json:
            query = request_json['query']
        else:
            raise ValueError("JSON is invalid, or missing a 'query' property")
    elif content_type == 'text/plain':
        query = request.data
    else:
        raise ValueError("Unknown content type: {}".format(content_type))
    
    options['query'] = query
    youtube_search(options)
    new_df = create_videos_dataframe()

    ## GCP get bucket and current file
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('buffme')
    blob = bucket.blob(FILE_PATH)
    if blob.exists():
      current_df = pd.read_csv(f"gs://{BUCKET_NAME}/{FILE_PATH}", encoding="utf-8", index_col="video_id")
      blob.upload_from_string(pd.concat([current_df, new_df]).drop_duplicates().to_csv(), 'text/csv')
    else:
      blob.upload_from_string(new_df.to_csv(), 'text/csv')

    return {
        "status": 200,
        "message": 'File has been written in buffme bucket under data/videos.csv'
    }

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=options['query'],
        part="id,snippet",
        maxResults=options['max_results']
    ).execute()

    # Add each result to the appropriate list, and then display the lists of
    # matching videos or channels
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append(search_result)
        elif search_result["id"]["kind"] == "youtube#channel":
            channels.append(search_result)

def create_videos_dataframe():
    df_youtube_videos = pd.DataFrame.from_dict(
        pd.json_normalize(videos), orient='columns')
    rename_dict = {
        'kind': 'type',
        'etag': 'asset_tag',
        'id.kind': 'asset_type',
        'id.videoId': 'video_id',
        'snippet.publishedAt': 'published_at',
        'snippet.channelId': 'channel_id',
        'snippet.title': 'title',
        'snippet.description': 'description',
        'snippet.thumbnails.default.url': 'thumbnail_default_url',
        'snippet.thumbnails.default.width': 'thumbnail_default_width',
        'snippet.thumbnails.default.height': 'thumbnail_default_height',
        'snippet.thumbnails.medium.url': 'thumbnail_medium_url',
        'snippet.thumbnails.medium.width': 'thumbnail_medium_width',
        'snippet.thumbnails.medium.height': 'thumbnail_medium_height',
        'snippet.thumbnails.high.url': 'thumbnail_high_url',
        'snippet.thumbnails.high.width': 'thumbnail_high_width',
        'snippet.thumbnails.high.height': 'thumbnail_high_height',
        'snippet.channelTitle': 'channel_title',
        'snippet.liveBroadcastContent': 'live_broadcast_content',
        'snippet.publishTime': 'published_time'
    }
    df_youtube_videos.rename(columns=rename_dict, inplace=True)
    df_youtube_videos.set_index('video_id', inplace=True)
    return df_youtube_videos
