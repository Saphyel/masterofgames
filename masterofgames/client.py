__strict__ = True

from typing import List

import httpx

from masterofgames.config import config
from masterofgames.entities import Game, GameAchievement, PlayerStats, PlayerAchievement, Player


async def client_fetch(endpoint: str, payload: dict | None = None) -> dict:
    if not payload:
        payload = {}
    payload.update({"key": config.steam_api_key})
    async with httpx.AsyncClient() as client:
        result = await client.get(config.steam_url + endpoint, params=payload, timeout=10)
        result.raise_for_status()
        return result.json()


async def find_player_games(user_id: str) -> List[Game]:
    result = await client_fetch("/IPlayerService/GetOwnedGames/v1/", {"steamid": user_id, "include_appinfo": "1"})
    return [Game(**game) for game in result["response"]["games"]]


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


async def find_user_id(name: str) -> str:
    result = await client_fetch("/ISteamUser/ResolveVanityURL/v1/", {"vanityurl": name})
    response = result["response"]
    if response["success"] != 1:
        raise ValueError(response["message"])
    return response["steamid"]


async def find_user_summary(user_id: str) -> Player:
    result = await client_fetch("/ISteamUser/GetPlayerSummaries/v2/", {"steamids": user_id})
    return Player(**result["response"]["players"][0])
