__strict__ = True

from unittest.mock import AsyncMock, Mock

from pytest import mark

from masterofgames.services import AchievementService, ProfileService
from tests import fixtures


@mark.asyncio
class TestProfileService:
    async def test_valid_user_data(self):
        response = Mock()
        response.json.return_value = fixtures.user_data()
        client = AsyncMock()
        client.get.return_value = response

        assert "666" == await ProfileService().get_user_id(client, "Saphyel", "steam_key")

    async def test_valid_summary_data(self):
        response = Mock()
        response.json.return_value = fixtures.profile_raw_data()
        client = AsyncMock()
        client.get.return_value = response
        assert fixtures.profile_data() == await ProfileService().get_profile(client, "666", "steam_key")


@mark.asyncio
class TestAchievementService:
    async def test_valid_player_progress_data(self):
        response = Mock()
        response.json.return_value = fixtures.achievement_raw_data()
        client = AsyncMock()
        client.get.return_value = response
        assert fixtures.achievement_data() == await AchievementService().get_achievements(
            client, "76561198109613067", "391220", "steam_key"
        )
