__strict__ = True

import functools
from typing import List

from requests import HTTPError

from crawlers.base import client_fetch
from models.model import GameAchievement, PlayerStats, PlayerAchievement


@functools.lru_cache
def find_game_details(game_id: str) -> List[GameAchievement]:
    result = client_fetch("/ISteamUserStats/GetSchemaForGame/v2/", {"appid": game_id})
    if result["game"] == {}:
        raise HTTPError("No details.")
    return [GameAchievement(**achievement) for achievement in result["game"]["availableGameStats"]["achievements"]]


@functools.lru_cache
def find_game_achievements(user_id: str, game_id: str) -> PlayerStats:
    result = client_fetch("/ISteamUserStats/GetPlayerAchievements/v1/", {"steamid": user_id, "appid": game_id})
    response = result["playerstats"]
    response["achievements"] = [PlayerAchievement(**achievement) for achievement in response["achievements"]]
    return PlayerStats(**response)
