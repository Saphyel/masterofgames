__strict__ = True

from unittest import TestCase, mock

from service import ProfileService, AchievementService
import fixtures
from requests_mock import MockResponse


class TestProfileService(TestCase):
    @mock.patch('requests.get', autospec=True, spec_set=True, return_value=MockResponse(403, {}))
    def test_invalid_token(self, mock_requests) -> None:
        with self.assertRaises(ValueError) as context:
            ProfileService().get_user_id('xxx')
        self.assertTrue('Invalid credentials' in str(context.exception))

    @mock.patch('requests.get', autospec=True, spec_set=True, return_value=MockResponse(500, {}))
    def test_server_down(self, mock_requests) -> None:
        with self.assertRaises(RuntimeError) as context:
            ProfileService().get_user_id('xxx')
        self.assertTrue('Server error' in str(context.exception))

    @mock.patch('requests.get', autospec=True, spec_set=True, return_value=MockResponse(200, fixtures.user_data()))
    def test_valid_user_data(self, mock_requests) -> None:
        self.assertEqual('666', ProfileService().get_user_id('xxx'))

    @mock.patch('requests.get', autospec=True, spec_set=True, return_value=MockResponse(200, fixtures.invalid_user_data()))
    def test_invalid_user_data(self, mock_requests) -> None:
        with self.assertRaises(ValueError) as context:
            ProfileService().get_user_id('lol')
        self.assertTrue('Not found' in str(context.exception))

    @mock.patch('requests.get', autospec=True, spec_set=True, return_value=MockResponse(200, fixtures.profile_raw_data()))
    def test_valid_summary_data(self, mock_requests) -> None:
        self.assertEqual(fixtures.profile_data(), ProfileService().get_profile('666'))


class TestAchievementService(TestCase):
    # @mock.patch('requests.get', autospec=True, spec_set=True, return_value=MockResponse(200, fixtures.empty_player_stats_data()))
    # def test_invalid_game_details_data(self, mock_requests) -> None:
    #     with self.assertRaises(ValueError) as context:
    #         AchievementService().get_achievements('666', '69')
    #     self.assertTrue('No stats' in str(context.exception))

    @mock.patch('requests.get', autospec=True, spec_set=True, return_value=MockResponse(200, fixtures.invalid_player_stats_data()))
    def test_invalid_player_progress_data(self, mock_requests) -> None:
        with self.assertRaises(ValueError) as context:
            AchievementService().get_achievements('666', '69')
        self.assertTrue('Requested app has no stats' in str(context.exception))

    # @mock.patch('requests.get', autospec=True, spec_set=True, return_value=MockResponse(200, fixtures.player_stats_data()))
    # def test_valid_player_progress_data(self, mock_requests) -> None:
    #     self.assertEqual(fixtures.player_stats_data()['playerstats']['achievements'], AchievementService().get_achievements('666', '69'))
    #
    # def test_invalid_game_details_data(self, mock_api) -> None:
    #     mock_api.fetch.return_value = {}
    #     with self.assertRaises(ValueError) as context:
    #         StatsRepository(mock_api).game_details('69')
    #     self.assertTrue('No stats' in str(context.exception))
    #
    # def test_valid_game_details_data(self, mock_api) -> None:
    #     mock_api.fetch.return_value = fixtures.game_stats_data()
    #     self.assertEqual(StatsRepository(mock_api).game_details('69'), fixtures.game_stats_data()['game'])
