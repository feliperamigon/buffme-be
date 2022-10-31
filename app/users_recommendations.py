import requests as r
import pandas as pd
import json
import numpy as np
from sklearn.manifold import TSNE
import plotly.express as px
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

def recommend_users(user):
    users = r.get("https://buffme-be-ca43ottweq-no.a.run.app/api/users")
    users_response = users.json()
    df_users = pd.DataFrame.from_dict(pd.json_normalize(users_response), orient='columns')
    filtered_df = df_users[
        ["platform_username",
        "lifetime_stats.wins.value",
        "lifetime_stats.bombsDefused.displayValue",
        "lifetime_stats.wlPercentage.value",
        "lifetime_stats.wlPercentage.displayValue"
        ]]
    numeric_df = filtered_df[
        ["lifetime_stats.wins.value",
        "lifetime_stats.bombsDefused.displayValue",
        "lifetime_stats.wlPercentage.value",
        "lifetime_stats.wlPercentage.displayValue"
        ]]
    numeric_df = numeric_df.replace(',','', regex=True)
    numeric_df["lifetime_stats.wlPercentage.displayValue"] = numeric_df["lifetime_stats.wlPercentage.displayValue"].str.replace('%', '')
    numeric_df["lifetime_stats.wlPercentage.displayValue"] = numeric_df["lifetime_stats.wlPercentage.displayValue"].str.replace(',', '.')
    numeric_df["lifetime_stats.wins.value"] = numeric_df["lifetime_stats.wins.value"].astype('int64')
    numeric_df["lifetime_stats.bombsDefused.displayValue"] = numeric_df["lifetime_stats.bombsDefused.displayValue"].astype('int64')
    numeric_df["lifetime_stats.wlPercentage.value"] = numeric_df["lifetime_stats.wlPercentage.value"].astype('float64')
    numeric_df["lifetime_stats.wlPercentage.displayValue"] = numeric_df["lifetime_stats.wlPercentage.displayValue"].astype('float64')
    return get_similar_users(numeric_df, filtered_df, user)

def get_similar_users(numeric_df, filtered_df, user):
    n_users = 4 # Since CS:GO is a 5vs5 game, recommend 4 + the current user
    neighbors = NearestNeighbors(n_neighbors= n_users, metric = "cosine")
    neighbors.fit(numeric_df)
    top_distancias, top_users = neighbors.kneighbors(numeric_df, return_distance=True)
    index = filtered_df[filtered_df['platform_username'] == user].index[0]
    recommended_users_list = filtered_df['platform_username'].loc[top_users[index]].values
    return recommended_users_list[1:].tolist()