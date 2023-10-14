__strict__ = True

from typing import List

import httpx

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

    async def get_achievements(self, client: httpx.AsyncClient, user_id: str, app_id: str, key: str) -> GameProgress:
        progression = await find_game_achievements(client, user_id, app_id, key)
        return GameProgress(
            name=progression.gameName,
            achievements=self._get_list(await find_game_details(client, app_id, key), progression.achievements),
        )


class ProfileService:
    async def get_user_id(self, client: httpx.AsyncClient, username: str, key: str) -> str:
        return await find_user_id(client, username, key)

    async def get_profile(self, client: httpx.AsyncClient, user_id: str, key: str) -> Profile:
        return Profile(
            player=await find_user_summary(client, user_id, key), games=await find_player_games(client, user_id, key)
        )
