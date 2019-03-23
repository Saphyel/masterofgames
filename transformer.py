from typing import List

from model_v1 import Profile, Game, Achievement


class ProfileTransformer:
    @staticmethod
    def transform(summary: dict) -> Profile:
        return Profile(summary['steamid'], summary['personaname'], summary['avatar'], summary['profileurl'],
                       summary['realname'], summary['loccountrycode'])


class GameTransformer:
    @staticmethod
    def transform(game_list: List[dict]) -> List[Game]:
        return [Game(item['appid'], item['name'], item['playtime_forever'], item['img_logo_url']) for item in game_list]


class AchievementTransformer:
    @staticmethod
    def transform(game_list: List[dict], player_list: List[dict]) -> List[Achievement]:
        items = len(game_list)
        print(items)
        print(len(player_list))
        if items != len(player_list):
            raise ValueError('Should match the list of both.')

        result = []
        for i in range(items):
            item = game_list[i]
            result.append(
                Achievement(item['name'], item['displayName'], item.get('description', ''), item['icon'],
                            item['hidden'] == 1, player_list[i]['achieved'] == 1))

        return result
