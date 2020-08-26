__strict__ = True

from unittest import TestCase, mock

from masterofgames.service import ProfileService, AchievementService
from masterofgames.repository import SteamClient, UserRepository, PlayerRepository, StatsRepository
import fixtures
from requests_mock import MockResponse


class TestProfileService(TestCase):
    @mock.patch('requests.get', autospec=True, spec_set=True, return_value=MockResponse(403, {}))
    def test_invalid_token(self, mock_requests) -> None:
        with self.assertRaises(ValueError) as context:
            ProfileService(UserRepository(SteamClient('xxx')), PlayerRepository(SteamClient('xxx'))).get_user_id('xxx')
        self.assertTrue('Invalid credentials' in str(context.exception))

    @mock.patch('requests.get', autospec=True, spec_set=True, return_value=MockResponse(500, {}))
    def test_server_down(self, mock_requests) -> None:
        with self.assertRaises(RuntimeError) as context:
            ProfileService(UserRepository(SteamClient('xxx')), PlayerRepository(SteamClient('xxx'))).get_user_id('xxx')
        self.assertTrue('Server error' in str(context.exception))

    @mock.patch('requests.get', autospec=True, spec_set=True, return_value=MockResponse(200, fixtures.user_data()))
    def test_valid_user_data(self, mock_requests) -> None:
        self.assertEqual(
            '666',
            ProfileService(UserRepository(SteamClient('xxx')), PlayerRepository(SteamClient('xxx'))).get_user_id('xxx')
        )

    @mock.patch('requests.get', autospec=True, spec_set=True, return_value=MockResponse(200, fixtures.invalid_user_data()))
    def test_invalid_user_data(self, mock_requests) -> None:
        with self.assertRaises(ValueError) as context:
            ProfileService(UserRepository(SteamClient('xxx')), PlayerRepository(SteamClient('xxx'))).get_user_id('lol')
        self.assertTrue('Not found' in str(context.exception))

    @mock.patch('requests.get', autospec=True, spec_set=True, return_value=MockResponse(200, fixtures.profile_raw_data()))
    def test_valid_summary_data(self, mock_requests) -> None:
        self.assertEqual(
            fixtures.profile_data(),
            ProfileService(UserRepository(SteamClient('xxx')), PlayerRepository(SteamClient('xxx'))).get_profile('666')
        )


class TestAchievementService(TestCase):
    @mock.patch('requests.get', autospec=True, spec_set=True, return_value=MockResponse(
        200,
        fixtures.invalid_player_stats_data()
    ))
    def test_invalid_player_progress_data(self, mock_requests) -> None:
        with self.assertRaises(ValueError) as context:
            AchievementService(StatsRepository(SteamClient('xxx'))).get_achievements('666', '69')
        self.assertTrue('Requested app has no stats' in str(context.exception))
