__strict__ = True

import functools
from typing import List

from crawlers.base import client_fetch
from models.model import Game


@functools.lru_cache
def find_player_games(user_id: str) -> List[Game]:
    result = client_fetch("/IPlayerService/GetOwnedGames/v1/", {"steamid": user_id, "include_appinfo": "1"})
    return [Game(**game) for game in result["response"]["games"]]
