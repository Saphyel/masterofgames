__strict__ = True

from crawlers.player import find_player_games
from crawlers.user import find_user_id, find_user_summary
from models.model import Profile


class ProfileService:
    async def get_user_id(self, username: str) -> str:
        return await find_user_id(username)

    async def get_profile(self, user_id: str) -> Profile:
        return Profile(await find_user_summary(user_id), await find_player_games(user_id))
