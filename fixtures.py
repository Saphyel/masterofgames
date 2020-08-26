__strict__ = True

from masterofgames.model import Profile, Game, Achievement


def user_data() -> dict:
    return {'response': {'steamid': '666', 'success': 1}}


def invalid_user_data() -> dict:
    return {'response': {'message': 'Not found', 'success': 42}}


def summary_data() -> dict:
    return {'response': {'players': [{
        'steamid': '76561198109613067',
        'communityvisibilitystate': 3,
        'profilestate': 1,
        'personaname': 'Saphyel',
        'lastlogoff': 1553126036,
        'profileurl': 'https://steamcommunity.com/id/Saphyel/',
        'avatar': 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/46'
                  '/464cde033aaa608ede90255f7dd869954aee68a4.jpg',
        'avatarmedium': 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/46'
                        '/464cde033aaa608ede90255f7dd869954aee68a4_medium.jpg',
        'avatarfull': 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/46'
                      '/464cde033aaa608ede90255f7dd869954aee68a4_full.jpg',
        'personastate': 0,
        'realname': 'Carlos',
        'primaryclanid': '103582791429521408',
        'timecreated': 1380828090,
        'personastateflags': 0,
        'loccountrycode': 'GB',
        'locstatecode': '17'
    }]}}


def player_data() -> dict:
    return {'response': {'game_count': 49, 'games': [
        {'appid': 219990, 'name': 'Grim Dawn', 'playtime_forever': 1534,
         'img_icon_url': '762057f2b14463ae1cbf0701a4cdb25cf94e8a0c',
         'img_logo_url': '8021ad6119b367593f1b1536aafd11397fb24ae9', 'has_community_visible_stats': True},
        {'appid': 340170, 'name': 'FINAL FANTASY TYPE-0 HD', 'playtime_forever': 121,
         'img_icon_url': 'f118decd2b35d1fc568bd5517db7d2d27dfc6b2f',
         'img_logo_url': '748e1a2bdfae60edc984f60c368bd665ead0f394', 'has_community_visible_stats': True},
        {'appid': 462780, 'name': 'Darksiders Warmastered Edition', 'playtime_forever': 2666,
         'img_icon_url': '4616a0d94eb5864f2933fd0157bb60a27b14d5fe',
         'img_logo_url': 'f188a32787983ef5346157473a4d8ba0ed024d98', 'has_community_visible_stats': True},
        {'appid': 391220, 'name': 'Rise of the Tomb Raider', 'playtime_2weeks': 531, 'playtime_forever': 4004,
         'img_icon_url': '0b8a37f32ed2b7c934be8aa94d53f71e274c6497',
         'img_logo_url': '5270d12abfc683e6f1d39e7ac0b6f2db366e7209', 'has_community_visible_stats': True},
        {'appid': 637650, 'name': 'FINAL FANTASY XV WINDOWS EDITION', 'playtime_forever': 20162,
         'img_icon_url': '0a99fcc7b08c7240d9146390cf1be28451aeef73',
         'img_logo_url': 'fb3a73c1b6a8305b5dc19110d14420d835956bc0', 'has_community_visible_stats': True},
        {'appid': 414340, 'name': "Hellblade: Senua's Sacrifice", 'playtime_forever': 746,
         'img_icon_url': '8a5d8f2d1cb52b21eaf4f6609592c6634731c962',
         'img_logo_url': 'e0e79fb1f259c84092119ef9b823914566ec457f', 'has_community_visible_stats': True},
        {'appid': 747350, 'name': "Hellblade: Senua's Sacrifice VR Edition", 'playtime_forever': 0,
         'img_icon_url': '8a5d8f2d1cb52b21eaf4f6609592c6634731c962',
         'img_logo_url': 'd644a74bacd0ecfedf6b68806c6ad6f6253a17fa', 'has_community_visible_stats': True},
    ]}}


def profile_raw_data() -> dict:
    return {'response': {
        'games': [
            {'appid': 219990, 'name': 'Grim Dawn', 'playtime_forever': 1534,
             'img_icon_url': '762057f2b14463ae1cbf0701a4cdb25cf94e8a0c',
             'img_logo_url': '8021ad6119b367593f1b1536aafd11397fb24ae9', 'has_community_visible_stats': True},
        ],
        'players': [{
            'steamid': '76561198109613067',
            'communityvisibilitystate': 3,
            'profilestate': 1,
            'personaname': 'Saphyel',
            'lastlogoff': 1553126036,
            'profileurl': 'https://steamcommunity.com/id/Saphyel/',
            'avatar': 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/46'
                      '/464cde033aaa608ede90255f7dd869954aee68a4.jpg',
            'avatarmedium': 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/46'
                            '/464cde033aaa608ede90255f7dd869954aee68a4_medium.jpg',
            'avatarfull': 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/46'
                          '/464cde033aaa608ede90255f7dd869954aee68a4_full.jpg',
            'personastate': 0,
            'realname': 'Carlos',
            'primaryclanid': '103582791429521408',
            'timecreated': 1380828090,
            'personastateflags': 0,
            'loccountrycode': 'GB',
            'locstatecode': '17'
        }]
    }}


def game_stats_data() -> dict:
    return {'game': {
        'gameName': 'Rise of the Tomb Raider',
        'gameVersion': '75',
        'availableGameStats': {
            'stats': [
                {'name': 'EquipmentCrafted', 'defaultvalue': 0, 'displayName': 'Equipment Crafted'},
                {'name': 'ChallengeTombsCompleted', 'defaultvalue': 0, 'displayName': 'Challenge Tombs Completed'},
                {'name': 'ChallengeCompleted', 'defaultvalue': 0, 'displayName': 'Challenges Completed'},
                {'name': 'ReplayMedalsGold', 'defaultvalue': 0, 'displayName': 'Score Attack Gold Medals'},
                {'name': 'BoltActionHeadshots', 'defaultvalue': 0, 'displayName': 'Bolt Action Headshots'},
                {'name': 'MissionCompleted', 'defaultvalue': 0, 'displayName': 'Missions Completed'},
                {'name': 'ArrowsCrafted', 'defaultvalue': 0, 'displayName': 'Arrows Crafted'},
                {'name': 'DeerHeadshots', 'defaultvalue': 0, 'displayName': 'Deer Headshots'},
                {'name': 'CardsCollected', 'defaultvalue': 0, 'displayName': 'Cards Collected'},
                {'name': 'PlayerHealed', 'defaultvalue': 0, 'displayName': 'Healed in Combat'},
                {'name': 'CollectiblesFound', 'defaultvalue': 0, 'displayName': 'Collectibles Found'},
                {'name': 'UpgradedWeapons', 'defaultvalue': 0, 'displayName': 'Fully Upgraded Weapons'},
                {'name': 'Untouchable', 'defaultvalue': 0, 'displayName': ''},
                {'name': 'BladeOfJustice', 'defaultvalue': 0, 'displayName': ''},
                {'name': 'TheWitchBottles', 'defaultvalue': 0, 'displayName': ''},
                {'name': 'SeasonOfTheWitch', 'defaultvalue': 0, 'displayName': ''},
                {'name': 'CompleteHistoryWitchCraft', 'defaultvalue': 0, 'displayName': ''},
                {'name': 'WitchHunt', 'defaultvalue': 0, 'displayName': ''},
                {'name': 'BravosLegacy', 'defaultvalue': 0, 'displayName': ''},
                {'name': 'DemonInTheDark', 'defaultvalue': 0, 'displayName': ''},
                {'name': 'WraithOfSiberia', 'defaultvalue': 0, 'displayName': ''},
                {'name': 'ReplayMedalsBabaYagaGold', 'defaultvalue': 0, 'displayName': ''},
                {'name': 'CompleteFamilyHistory', 'defaultvalue': 0, 'displayName': 'Documents found'},
                {'name': 'FightTheFear', 'defaultvalue': 0, 'displayName': 'Enemies killed'},
                {'name': 'MeetTheCrofts', 'defaultvalue': 0, 'displayName': 'Documents found'},
                {'name': 'RelicHunter', 'defaultvalue': 0, 'displayName': 'Relics found'}
            ],
            'achievements': [
                {'name': 'NEW_ACHIEVEMENT_3_1', 'defaultvalue': 0, 'displayName': 'Bar Brawl', 'hidden': 0,
                 'description': 'Melee kill an enemy using a bottle',
                 'icon': 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/391220'
                         '/5cb2c2984f03fc1acd72126741b4141ebbc239f1.jpg',
                 'icongray': 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/391220'
                             '/753ca3075e7fec8d6d339335bacd6681980977ce.jpg'},
                {'name': 'NEW_ACHIEVEMENT_3_2', 'defaultvalue': 0, 'displayName': 'Blade of Justice', 'hidden': 0,
                 'description': 'Perform 25 special stealth kills with the knife',
                 'icon': 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/391220'
                         '/918bba7906d55ceff7179ded663d499a4fcf6c84.jpg',
                 'icongray': 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/391220'
                             '/a26ad571230e938f5fdc912729bb3f0b309894b6.jpg'}
            ]
        }
    }}


def player_stats_data() -> dict:
    return {'playerstats': {
        'steamID': '76561198109613067',
        'gameName': 'Rise of the Tomb Raider',
        'achievements': [
            {'apiname': 'NEW_ACHIEVEMENT_3_1', 'achieved': 1, 'unlocktime': 1546695765},
            {'apiname': 'NEW_ACHIEVEMENT_3_2', 'achieved': 1, 'unlocktime': 1546342474}
        ],
        'success': True
    }}


def invalid_player_stats_data() -> dict:
    return {'playerstats': {'error': 'Requested app has no stats', 'success': False}}


def empty_player_stats_data() -> dict:
    return {'playerstats': {}}


def profile_data() -> Profile:
    data = summary_data()['response']['players'][0]
    return Profile(data['steamid'], data['personaname'], data['avatar'], data['profileurl'], data['realname'],
                   data['loccountrycode'], [game_data()])


def game_data() -> Game:
    data = player_data()['response']['games'][0]
    return Game(data['appid'], data['name'], data['playtime_forever'], data['img_logo_url'])


def achievement_data() -> Achievement:
    data1 = game_stats_data()['game']['availableGameStats']['achievements'][0]
    data2 = player_stats_data()['playerstats']['achievements'][0]
    return Achievement(data1['name'], data1['displayName'], data1.get('description', ''), data1['icon'],
                       data1['hidden'] == 1, data2['achieved'] == 1)
