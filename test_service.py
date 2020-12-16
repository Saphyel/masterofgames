__strict__ = True

from unittest import TestCase, mock

import fixtures
from masterofgames.service import ProfileService, AchievementService


class TestProfileService(TestCase):
    @mock.patch(
        "masterofgames.repository.client_fetch", autospec=True, spec_set=True, return_value=fixtures.user_data()
    )
    def test_valid_user_data(self, mock_requests) -> None:
        self.assertEqual("666", ProfileService().get_user_id("Saphyel"))

    @mock.patch(
        "masterofgames.repository.client_fetch", autospec=True, spec_set=True, return_value=fixtures.profile_raw_data()
    )
    def test_valid_summary_data(self, mock_requests) -> None:
        self.assertEqual(fixtures.profile_data(), ProfileService().get_profile("666"))


# class TestAchievementService(TestCase):
#     @mock.patch(
#         "masterofgames.repository.client_fetch",
#         autospec=True,
#         spec_set=True,
#         return_value=fixtures.player_stats_data(),
#     )
#     def test_valid_player_progress_data(self, mock_requests) -> None:
#         self.assertEqual(fixtures.profile_data(), AchievementService().get_achievements("76561198109613067", "391220"))
