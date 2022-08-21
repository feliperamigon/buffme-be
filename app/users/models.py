import json


class User:
    def __init__(self, avatar, platform_slug, platform_username, platform_user_id):
        self.avatar = avatar
        self.platform_slug = platform_slug
        self.platform_username = platform_username
        self.platform_user_id = platform_user_id

    def __iter__(self):
        yield 'avatar', self.avatar
        yield 'platform_slug', self.platform_slug
        yield 'platform_username', self.platform_username
        yield 'platform_user_id', self.platform_user_id

    def serializeToJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
