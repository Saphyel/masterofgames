__strict__ = True

from unittest.mock import AsyncMock, patch

from pytest import mark

from crud.achievement import AchievementService
from crud.profile import ProfileService
from tests import fixtures


@mark.asyncio
class TestProfileService:
    @patch("crawlers.user.client_fetch", return_value=fixtures.user_data(), new_callable=AsyncMock)
    async def test_valid_user_data(self, mock_requests) -> None:
        assert "666" == await ProfileService().get_user_id("Saphyel")

    @patch("crawlers.user.client_fetch", new_callable=AsyncMock, return_value=fixtures.profile_raw_data())
    @patch("crawlers.player.client_fetch", new_callable=AsyncMock, return_value=fixtures.profile_raw_data())
    async def test_valid_summary_data(self, mock_requests, mock_requests2) -> None:
        assert fixtures.profile_data() == await ProfileService().get_profile("666")


@mark.asyncio
class TestAchievementService:
    @patch("crawlers.stats.client_fetch", new_callable=AsyncMock, return_value=fixtures.achievement_raw_data())
    async def test_valid_player_progress_data(self, mock_requests) -> None:
        assert fixtures.achievement_data() == await AchievementService().get_achievements("76561198109613067", "391220")
