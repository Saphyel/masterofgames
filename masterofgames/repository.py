__strict__ = True

import functools
import os
import requests
from typing import List

from masterofgames.model import Player, Game, GameAchievement, PlayerStats, PlayerAchievement


steam_api_key = os.environ.get("STEAM_API_KEY")


def client_fetch(endpoint: str, payload: dict = None) -> dict:
    payload.update({"key": steam_api_key})
    result = requests.get("https://api.steampowered.com" + endpoint, params=payload, timeout=10)
    result.raise_for_status()
    return result.json()


@functools.lru_cache
def user_repository_find_user_id(name: str) -> str:
    result = client_fetch("/ISteamUser/ResolveVanityURL/v1/", {"vanityurl": name})
    response = result["response"]
    if response["success"] != 1:
        raise ValueError(response["message"])
    return response["steamid"]


@functools.lru_cache
def user_repository_find_summary(user_id: str) -> Player:
    result = client_fetch("/ISteamUser/GetPlayerSummaries/v2/", {"steamids": user_id})
    return Player(**result["response"]["players"][0])


@functools.lru_cache
def player_repository_find_games(user_id: str) -> List[Game]:
    result = client_fetch("/IPlayerService/GetOwnedGames/v1/", {"steamid": user_id, "include_appinfo": "1"})
    return [Game(**game) for game in result["response"]["games"]]


@functools.lru_cache
def stats_repository_find_details(game_id: str) -> List[GameAchievement]:
    result = client_fetch("/ISteamUserStats/GetSchemaForGame/v2/", {"appid": game_id})
    if result == {}:
        raise ValueError("No stats")
    return [GameAchievement(**achievement) for achievement in result["game"]["availableGameStats"]["achievements"]]


@functools.lru_cache
def stats_repository_find_achievements(user_id: str, game_id: str) -> PlayerStats:
    result = client_fetch("/ISteamUserStats/GetPlayerAchievements/v1/", {"steamid": user_id, "appid": game_id})
    response = result["playerstats"]
    if not response["success"]:
        raise ValueError(response["error"])
    response["achievements"] = [PlayerAchievement(**achievement) for achievement in response["achievements"]]
    return PlayerStats(**response)
