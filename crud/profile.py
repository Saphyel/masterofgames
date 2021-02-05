__strict__ = True

from crawlers.repository import UserRepository, PlayerRepository
from models.transformer import ProfileTransformer, GameTransformer


class ProfileService:
    def __init__(self, user_repository: UserRepository, player_repository: PlayerRepository):
        self._user_repository = user_repository
        self._profile_transformer = ProfileTransformer
        self._player_repository = player_repository
        self._game_transformer = GameTransformer

    def get_user_id(self, username: str):
        return self._user_repository.find_user_id(username)

    def get_profile(self, user_id: str):
        summary = self._user_repository.get_summary(user_id)
        games = [self._game_transformer.transform(game) for game in self._player_repository.find_games(user_id)]
        summary["games"] = games
        return self._profile_transformer.transform(summary)
