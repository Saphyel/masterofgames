__strict__ = True

import requests

from core.config import Config


def client_fetch(endpoint: str, payload: dict = None) -> dict:
    payload.update({"key": Config.STEAM_API_KEY})
    result = requests.get("https://api.steampowered.com" + endpoint, params=payload, timeout=10)
    result.raise_for_status()
    return result.json()
