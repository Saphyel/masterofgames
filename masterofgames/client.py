__strict__ = True

from typing import List

import httpx

from masterofgames.entities import Game, GameAchievement, PlayerStats, PlayerAchievement, Player


async def find_player_games(client: httpx.AsyncClient, user_id: str, key: str) -> List[Game]:
    result = await client.get(
        "/IPlayerService/GetOwnedGames/v1/", params={"steamid": user_id, "include_appinfo": "1", "key": key}
    )
    result = result.json()
    return [Game(**game) for game in result["response"]["games"]]


async def find_game_details(client: httpx.AsyncClient, game_id: str, key: str) -> List[GameAchievement]:
    result = await client.get("/ISteamUserStats/GetSchemaForGame/v2/", params={"appid": game_id, "key": key})
    result = result.json()
    if result["game"] == {}:
        raise ValueError("No details")
    return [GameAchievement(**achievement) for achievement in result["game"]["availableGameStats"]["achievements"]]


async def find_game_achievements(client: httpx.AsyncClient, user_id: str, game_id: str, key: str) -> PlayerStats:
    result = await client.get(
        "/ISteamUserStats/GetPlayerAchievements/v1/", params={"steamid": user_id, "appid": game_id, "key": key}
    )
    result = result.json()
    response = result["playerstats"]
    response["achievements"] = [PlayerAchievement(**achievement) for achievement in response["achievements"]]
    return PlayerStats(**response)


async def find_user_id(client: httpx.AsyncClient, name: str, key: str) -> str:
    result = await client.get("/ISteamUser/ResolveVanityURL/v1/", params={"vanityurl": name, "key": key})
    result = result.json()
    response = result["response"]
    if response["success"] != 1:
        raise ValueError(response["message"])
    return response["steamid"]


async def find_user_summary(client: httpx.AsyncClient, user_id: str, key: str) -> Player:
    result = await client.get("/ISteamUser/GetPlayerSummaries/v2/", params={"steamids": user_id, "key": key})
    result = result.json()
    return Player(**result["response"]["players"][0])
