__strict__ = True

from typing import List

from masterofgames.client import (
    find_player_games,
    find_game_achievements,
    find_game_details,
    find_user_id,
    find_user_summary,
)
from masterofgames.entities import GameAchievement, PlayerAchievement, Achievement, GameProgress, Profile


class AchievementService:
    def _get_list(self, details: List[GameAchievement], progression: List[PlayerAchievement]) -> List[Achievement]:
        items = len(details)
        result = []
        for i in range(items):
            detail = details[i]
            progress = progression[i]

            result.append(
                Achievement(
                    id=detail.name,
                    name=detail.displayName,
                    icon=detail.icon,
                    hidden=detail.hidden == 1,
                    achieved=progress.achieved == 1,
                    description=detail.description,
                )
            )

        return result

    async def get_achievements(self, user_id: str, app_id: str) -> GameProgress:
        progression = await find_game_achievements(user_id, app_id)
        return GameProgress(
            name=progression.gameName,
            achievements=self._get_list(await find_game_details(app_id), progression.achievements),
        )


class ProfileService:
    async def get_user_id(self, username: str) -> str:
        return await find_user_id(username)

    async def get_profile(self, user_id: str) -> Profile:
        return Profile(player=await find_user_summary(user_id), games=await find_player_games(user_id))
