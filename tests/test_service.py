__strict__ = True

from unittest import TestCase, mock

from crud.achievement import AchievementService
from crud.profile import ProfileService
from tests import fixtures


class TestProfileService(TestCase):
    @mock.patch("crawlers.user.client_fetch", autospec=True, spec_set=True, return_value=fixtures.user_data())
    def test_valid_user_data(self, mock_requests) -> None:
        self.assertEqual("666", ProfileService().get_user_id("Saphyel"))

    @mock.patch("crawlers.user.client_fetch", autospec=True, spec_set=True, return_value=fixtures.profile_raw_data())
    @mock.patch("crawlers.player.client_fetch", autospec=True, spec_set=True, return_value=fixtures.profile_raw_data())
    def test_valid_summary_data(self, mock_requests, mock_requests2) -> None:
        self.assertEqual(fixtures.profile_data(), ProfileService().get_profile("666"))


class TestAchievementService(TestCase):
    @mock.patch(
        "crawlers.stats.client_fetch",
        autospec=True,
        spec_set=True,
        return_value=fixtures.achievement_raw_data(),
    )
    def test_valid_player_progress_data(self, mock_requests) -> None:
        self.assertEqual(
            fixtures.achievement_data(), AchievementService().get_achievements("76561198109613067", "391220")
        )
