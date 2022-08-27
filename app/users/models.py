import json


class User:
    def __init__(self, avatar, platform_slug, platform_username, platform_user_id, lifetime_stats):
        self.avatar = avatar
        self.platform_slug = platform_slug
        self.platform_username = platform_username
        self.platform_user_id = platform_user_id
        self.lifetime_stats = lifetime_stats

    def __iter__(self):
        yield 'avatar', self.avatar
        yield 'platform_slug', self.platform_slug
        yield 'platform_username', self.platform_username
        yield 'platform_user_id', self.platform_user_id
        yield 'lifetime_stats', self.lifetime_stats

    def serialize_to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Stats:
    def __init__(self, platform_user_id, stats):
        self.platform_user_id = platform_user_id
        self.stats = stats

    def __iter__(self):
        yield 'platform_user_id', self.platform_user_id
        yield 'stats', self.stats

    def serialize_to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
