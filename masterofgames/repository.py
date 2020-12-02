__strict__ = True

import requests


# Wrapper
class SteamClient:
    def __init__(self, secret: str):
        self._secret = secret
        self._base_url = "https://api.steampowered.com/"

    def fetch(self, endpoint: str, payload: dict = None) -> dict:
        payload.update({"key": self._secret})
        result = requests.get(self._base_url + endpoint, params=payload, timeout=3)
        if result.status_code == 403:
            raise ValueError("Invalid credentials")
        if result.status_code >= 500:
            raise RuntimeError("Server error")
        return result.json()


# Read from external source
class UserRepository:
    RESOURCE = "ISteamUser/"

    def __init__(self, client: SteamClient):
        self._client = client

    def find_user_id(self, name: str) -> str:
        result = self._client.fetch(self.RESOURCE + "ResolveVanityURL/v1/", {"vanityurl": name})
        response = result["response"]
        if response["success"] != 1:
            raise ValueError(response["message"])
        return response["steamid"]

    def get_summary(self, user_id: str) -> dict:
        result = self._client.fetch(self.RESOURCE + "GetPlayerSummaries/v2/", {"steamids": user_id})
        return result["response"]["players"][0]


class PlayerRepository:
    RESOURCE = "IPlayerService/"

    def __init__(self, client: SteamClient):
        self._client = client

    def find_games(self, user_id: str) -> list:
        result = self._client.fetch(self.RESOURCE + "GetOwnedGames/v1/", {"steamid": user_id, "include_appinfo": "1"})
        return result["response"]["games"]


class StatsRepository:
    RESOURCE = "ISteamUserStats/"

    def __init__(self, client: SteamClient):
        self._client = client

    def game_details(self, game_id: str) -> list:
        result = self._client.fetch(self.RESOURCE + "GetSchemaForGame/v2/", {"appid": game_id})
        if result == {}:
            raise ValueError("No stats")
        return result["game"]["availableGameStats"]["achievements"]

    def find_achievements(self, user_id: str, game_id: str) -> dict:
        result = self._client.fetch(self.RESOURCE + "GetPlayerAchievements/v1/", {"steamid": user_id, "appid": game_id})
        response = result["playerstats"]
        if not response["success"]:
            raise ValueError(response["error"])
        return response
