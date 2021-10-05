__strict__ = True

from typing import List

from crawlers.base import client_fetch
from models.model import GameAchievement, PlayerStats, PlayerAchievement


async def find_game_details(game_id: str) -> List[GameAchievement]:
    result = await client_fetch("/ISteamUserStats/GetSchemaForGame/v2/", {"appid": game_id})
    if result["game"] == {}:
        raise ValueError("No details")
    return [GameAchievement(**achievement) for achievement in result["game"]["availableGameStats"]["achievements"]]


async def find_game_achievements(user_id: str, game_id: str) -> PlayerStats:
    result = await client_fetch("/ISteamUserStats/GetPlayerAchievements/v1/", {"steamid": user_id, "appid": game_id})
    response = result["playerstats"]
    response["achievements"] = [PlayerAchievement(**achievement) for achievement in response["achievements"]]
    return PlayerStats(**response)
