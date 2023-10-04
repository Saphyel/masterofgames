__strict__ = True

from masterofgames.crawlers.base import client_fetch
from masterofgames.models.model import Player


async def find_user_id(name: str) -> str:
    result = await client_fetch("/ISteamUser/ResolveVanityURL/v1/", {"vanityurl": name})
    response = result["response"]
    if response["success"] != 1:
        raise ValueError(response["message"])
    return response["steamid"]


async def find_user_summary(user_id: str) -> Player:
    result = await client_fetch("/ISteamUser/GetPlayerSummaries/v2/", {"steamids": user_id})
    return Player(**result["response"]["players"][0])
