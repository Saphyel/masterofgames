__strict__ = True

import functools

from crawlers.base import client_fetch
from models.model import Player


@functools.lru_cache
def find_user_id(name: str) -> str:
    result = client_fetch("/ISteamUser/ResolveVanityURL/v1/", {"vanityurl": name})
    response = result["response"]
    if response["success"] != 1:
        raise ValueError(response["message"])
    return response["steamid"]


@functools.lru_cache
def find_user_summary(user_id: str) -> Player:
    result = client_fetch("/ISteamUser/GetPlayerSummaries/v2/", {"steamids": user_id})
    return Player(**result["response"]["players"][0])
