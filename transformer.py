__strict__ = True

from model import Profile, Game, Achievement, GameProgress


class ProfileTransformer:
    @staticmethod
    def transform(summary: dict) -> Profile:
        return Profile(summary['steamid'], summary['personaname'], summary['avatar'], summary['profileurl'],
                       summary['realname'], summary['loccountrycode'], summary['games'])


class GameTransformer:
    @staticmethod
    def transform(game: dict) -> Game:
        return Game(game['appid'], game['name'], game['playtime_forever'], game['img_logo_url'])


class AchievementTransformer:
    @staticmethod
    def transform(achievement: dict) -> Achievement:
        return Achievement(achievement['name'], achievement['displayName'], achievement.get('description', ''),
                           achievement['icon'], achievement['hidden'] == 1, achievement['achieved'] == 1)


class GameProgressTransformer:
    @staticmethod
    def transform(progress: dict) -> GameProgress:
        return GameProgress(progress['title'], progress['achievements'])
