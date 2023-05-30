__strict__ = True

from typing import List

from src.crawlers.base import client_fetch
from src.models.model import Game


async def find_player_games(user_id: str) -> List[Game]:
    result = await client_fetch("/IPlayerService/GetOwnedGames/v1/", {"steamid": user_id, "include_appinfo": "1"})
    return [Game(**game) for game in result["response"]["games"]]
