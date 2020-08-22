__strict__ = True

from repository import UserRepository, PlayerRepository, StatsRepository
from transformer import ProfileTransformer, GameTransformer, AchievementTransformer, GameProgressTransformer


class ProfileService:
    def __init__(self):
        self._user_repository = UserRepository()
        self._profile_transformer = ProfileTransformer
        self._player_repository = PlayerRepository()
        self._game_transformer = GameTransformer

    def get_user_id(self, username: str):
        return self._user_repository.find_user_id(username)

    def get_profile(self, user_id: str):
        summary = self._user_repository.get_summary(user_id)
        games = [self._game_transformer.transform(game) for game in self._player_repository.find_games(user_id)]
        summary['games'] = games
        return self._profile_transformer.transform(summary)


class AchievementService:
    def __init__(self):
        self._repository = StatsRepository()
        self._game_transformer = GameProgressTransformer
        self._achievement_transformer = AchievementTransformer

    def _get_list(self, details: list, progression: dict):
        items = len(details)
        result = []
        for i in range(items):
            detail = details[i]
            progress = progression['achievements'][i]

            result.append(self._achievement_transformer.transform({**detail, **progress}))

        return result

    def get_achievements(self, user_id: str, app_id: str):
        progression = self._repository.find_achievements(user_id, app_id)
        return self._game_transformer.transform({'title': progression['gameName'],
                                                 'achievements': self._get_list(self._repository.game_details(app_id),
                                                                                progression)})
