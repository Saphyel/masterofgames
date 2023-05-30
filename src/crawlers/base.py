__strict__ = True

import httpx

from src.core.config import Config


async def client_fetch(endpoint: str, payload: dict = None) -> dict:
    payload.update({"key": Config.STEAM_API_KEY})
    async with httpx.AsyncClient() as client:
        result = await client.get("https://api.steampowered.com" + endpoint, params=payload, timeout=10)
        result.raise_for_status()
        return result.json()
