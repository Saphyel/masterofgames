from unittest import TestCase, mock

import fixtures
from steam_api import SteamAPI, UserRepository, PlayerRepository, StatsRepository


class MockResponse:
    def __init__(self, valid: bool, result: dict):
        self._valid = valid
        self._content = result

    @property
    def ok(self) -> bool:
        return self._valid

    @property
    def text(self) -> str:
        return 'error'

    def json(self):
        return self._content


@mock.patch('steam_api.Config')
class TestApi(TestCase):
    @mock.patch('requests.get', autospec=True, spec_set=True, return_value=MockResponse(True, fixtures.user_data()))
    def test_valid_user_data(self, mock_requests, mock_config) -> None:
        self.assertEqual(fixtures.user_data(), SteamAPI(mock_config).fetch('ISteamUser/', {'vanity': 'xxx'}))

    @mock.patch('requests.get', autospec=True, spec_set=True, return_value=MockResponse(False, fixtures.user_data()))
    def test_invalid_user_data(self, mock_requests, mock_config) -> None:
        with self.assertRaises(RuntimeError) as context:
            SteamAPI(mock_config).fetch('ISteamUser/', {'vanity': 'x'})
        self.assertTrue('error' in str(context.exception))


@mock.patch('steam_api.SteamAPI', autospec=True, spec_set=True)
class TestUserRepository(TestCase):
    def test_valid_user_data(self, mock_api) -> None:
        mock_api.fetch.return_value = fixtures.user_data()
        self.assertEqual(UserRepository(mock_api).find_user_id('lol'), fixtures.user_data()['response']['steamid'])

    def test_invalid_user_data(self, mock_api) -> None:
        mock_api.fetch.return_value = fixtures.invalid_user_data()
        with self.assertRaises(ValueError) as context:
            UserRepository(mock_api).find_user_id('lol')
        self.assertTrue('Not found' in str(context.exception))

    def test_valid_summary_data(self, mock_api) -> None:
        mock_api.fetch.return_value = fixtures.summary_data()
        self.assertEqual(UserRepository(mock_api).get_summary('666'), fixtures.summary_data()['response']['players'][0])


@mock.patch('steam_api.SteamAPI', autospec=True, spec_set=True)
class TestPlayerRepository(TestCase):
    def test_valid_player_data(self, mock_api) -> None:
        mock_api.fetch.return_value = fixtures.player_data()
        self.assertEqual(PlayerRepository(mock_api).find_games('666'), fixtures.player_data()['response']['games'])


@mock.patch('steam_api.SteamAPI', autospec=True, spec_set=True)
class TestStatsRepository(TestCase):
    def test_valid_game_details_data(self, mock_api) -> None:
        mock_api.fetch.return_value = fixtures.game_stats_data()
        self.assertEqual(StatsRepository(mock_api).game_details('69'), fixtures.game_stats_data()['game'])

    def test_valid_player_progress_data(self, mock_api) -> None:
        mock_api.fetch.return_value = fixtures.player_stats_data()
        self.assertEqual(StatsRepository(mock_api).player_progress('666', '69'),
                         fixtures.player_stats_data()['playerstats']['achievements'])
