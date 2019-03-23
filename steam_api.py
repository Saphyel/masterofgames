import requests

from config import Config


# Wrapper
class SteamAPI:
    def __init__(self, config: Config):
        self._key = config.key
        self._base_url = config.base_url

    def fetch(self, endpoint: str, payload: dict = {}) -> dict:
        payload.update({'key': self._key})
        result = requests.get(self._base_url + endpoint, params=payload, timeout=3)
        if not result.ok:
            raise RuntimeError(result.text)
        return result.json()


# Read from external source
class UserRepository:
    RESOURCE = 'ISteamUser/'

    def __init__(self, client: SteamAPI):
        self._client = client

    def find_user_id(self, name: str) -> str:
        result = self._client.fetch(self.RESOURCE + 'ResolveVanityURL/v1/', {'vanityurl': name})
        response = result['response']
        if response['success'] != 1:
            raise ValueError(response['message'])
        return response['steamid']

    def get_summary(self, user_id: str) -> dict:
        result = self._client.fetch(self.RESOURCE + 'GetPlayerSummaries/v2/', {'steamids': user_id})
        return result['response']['players'][0]


class PlayerRepository:
    RESOURCE = 'IPlayerService/'

    def __init__(self, client: SteamAPI):
        self.client = client

    def find_games(self, user_id: str) -> list:
        result = self.client.fetch(self.RESOURCE + 'GetOwnedGames/v1/', {'steamid': user_id, 'include_appinfo': '1'})
        return result['response']['games']


class StatsRepository:
    RESOURCE = 'ISteamUserStats/'

    def __init__(self, client: SteamAPI):
        self.client = client

    def game_details(self, game_id: str) -> dict:
        result = self.client.fetch(self.RESOURCE + 'GetSchemaForGame/v2/', {'appid': game_id})
        return result['game']

    def player_progress(self, user_id: str, game_id: str) -> list:
        result = self.client.fetch(self.RESOURCE + 'GetPlayerAchievements/v1/', {'steamid': user_id, 'appid': game_id})
        return result['playerstats']['achievements']


if __name__ == '__main__':
    appId = '391220'
    userId = '76561198109613067'

    api = SteamAPI(Config())
    # lol = api.fetch('ISteamUser/ResolveVanityURL/v1/', {'vanityurl': 'Saphyel'})
    # PlayerRepository(api).find_games(userId)
    # UserRepository(api).get_summary(userId)
    # StatsRepository(api).game_details(appId)
    # StatsRepository(api).player_progress(userId, appId)
