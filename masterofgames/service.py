__strict__ = True

from typing import List

from .model import GameProgress, Profile, PlayerAchievement, GameAchievement, Achievement
from .repository import (
    user_repository_find_user_id,
    user_repository_find_summary,
    player_repository_find_games,
    stats_repository_find_achievements,
    stats_repository_find_details,
)


class ProfileService:
    def get_user_id(self, username: str) -> str:
        return user_repository_find_user_id(username)

    def get_profile(self, user_id: str) -> Profile:
        return Profile(user_repository_find_summary(user_id), player_repository_find_games(user_id))


class AchievementService:
    def _get_list(self, details: List[GameAchievement], progression: List[PlayerAchievement]) -> List[Achievement]:
        items = len(details)
        result = []
        for i in range(items):
            detail = details[i]
            progress = progression[i]

            result.append(
                Achievement(
                    detail.name,
                    detail.displayName,
                    detail.icon,
                    detail.hidden == 1,
                    progress.achieved == 1,
                    detail.description,
                )
            )

        return result

    def get_achievements(self, user_id: str, app_id: str) -> GameProgress:
        progression = stats_repository_find_achievements(user_id, app_id)
        return GameProgress(
            progression.gameName, self._get_list(stats_repository_find_details(app_id), progression.achievements)
        )
