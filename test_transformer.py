from unittest import TestCase

import fixtures
from transformer import ProfileTransformer, GameTransformer, AchievementTransformer


class TesProfileTransformer(TestCase):
    def test_transform_summary_to_profile(self) -> None:
        self.assertEqual(fixtures.profile_data(),
                         ProfileTransformer.transform(fixtures.summary_data()['response']['players'][0]))


class TestGameTransformer(TestCase):
    def test_transform_list_to_gamer_list(self) -> None:
        self.assertEqual(fixtures.game_data(),
                         GameTransformer.transform(fixtures.player_data()['response']['games'])[0])


class TestAchievementTransformer(TestCase):
    def test_invalid_data(self) -> None:
        with self.assertRaises(ValueError) as context:
            AchievementTransformer.transform([{}], fixtures.player_stats_data()['playerstats']['achievements'])
        self.assertTrue('Should match the list of both.' in str(context.exception))

    def test_transform_scattered_data_to_achievements(self) -> None:
        self.assertEqual(fixtures.achievement_data(), AchievementTransformer.transform(
            fixtures.game_stats_data()['game']['availableGameStats']['achievements'],
            fixtures.player_stats_data()['playerstats']['achievements'])[0])
