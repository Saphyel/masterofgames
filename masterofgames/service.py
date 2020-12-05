__strict__ = True

from .model import GameProgress, Profile
from .repository import (
    user_repository_find_user_id,
    user_repository_find_summary,
    player_repository_find_games,
    stats_repository_find_achievements,
    stats_repository_find_details,
)
from .transformer import ProfileTransformer, GameTransformer, AchievementTransformer, GameProgressTransformer


class ProfileService:
    def __init__(self):
        self._profile_transformer = ProfileTransformer
        self._game_transformer = GameTransformer

    def get_user_id(self, username: str) -> str:
        return user_repository_find_user_id(username)

    def get_profile(self, user_id: str) -> Profile:
        summary = user_repository_find_summary(user_id)
        games = [self._game_transformer.transform(game) for game in player_repository_find_games(user_id)]
        summary["games"] = games
        return self._profile_transformer.transform(summary)


class AchievementService:
    def __init__(self):
        self._game_transformer = GameProgressTransformer
        self._achievement_transformer = AchievementTransformer

    def _get_list(self, details: list, progression: dict) -> list:
        items = len(details)
        result = []
        for i in range(items):
            detail = details[i]
            progress = progression["achievements"][i]

            result.append(self._achievement_transformer.transform({**detail, **progress}))

        return result

    def get_achievements(self, user_id: str, app_id: str) -> GameProgress:
        progression = stats_repository_find_achievements(user_id, app_id)
        return self._game_transformer.transform(
            {
                "title": progression["gameName"],
                "achievements": self._get_list(stats_repository_find_details(app_id), progression),
            }
        )
