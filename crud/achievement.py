__strict__ = True

from crawlers.repository import StatsRepository
from models.transformer import GameProgressTransformer, AchievementTransformer


class AchievementService:
    def __init__(self, repository: StatsRepository):
        self._repository = repository
        self._game_transformer = GameProgressTransformer
        self._achievement_transformer = AchievementTransformer

    def _get_list(self, details: list, progression: dict):
        items = len(details)
        result = []
        for i in range(items):
            detail = details[i]
            progress = progression["achievements"][i]

            result.append(self._achievement_transformer.transform({**detail, **progress}))

        return result

    def get_achievements(self, user_id: str, app_id: str):
        progression = self._repository.find_achievements(user_id, app_id)
        return self._game_transformer.transform(
            {
                "title": progression["gameName"],
                "achievements": self._get_list(self._repository.game_details(app_id), progression),
            }
        )
