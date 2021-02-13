__strict__ = True

from crawlers.player import find_player_games
from crawlers.user import find_user_id, find_user_summary
from models.model import Profile


class ProfileService:
    def get_user_id(self, username: str) -> str:
        return find_user_id(username)

    def get_profile(self, user_id: str) -> Profile:
        return Profile(find_user_summary(user_id), find_player_games(user_id))
