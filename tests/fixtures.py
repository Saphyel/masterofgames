__strict__ = True

from masterofgames.entities import Profile, Player, Game, GameProgress, Achievement


def user_data() -> dict:
    return {"response": {"steamid": "666", "success": 1}}


def summary_data() -> dict:
    return {
        "response": {
            "players": [
                {
                    "steamid": "76561198109613067",
                    "profilestate": 1,
                    "personaname": "Saphyel",
                    "lastlogoff": 1553126036,
                    "profileurl": "https://steamcommunity.com/id/Saphyel/",
                    "avatar": "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/46"
                    "/464cde033aaa608ede90255f7dd869954aee68a4.jpg",
                    "realname": "Carlos",
                    "timecreated": 1380828090,
                    "loccountrycode": "GB",
                    "communityvisibilitystate": 3,
                    "avatarmedium": "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/46"
                    "/464cde033aaa608ede90255f7dd869954aee68a4_medium.jpg",
                    "avatarfull": "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/46"
                    "/464cde033aaa608ede90255f7dd869954aee68a4_full.jpg",
                    "avatarhash": "111",
                    "personastate": 0,
                    "primaryclanid": "103582791429521408",
                    "personastateflags": 0,
                    "locstatecode": "17",
                }
            ]
        }
    }


def player_data() -> dict:
    return {
        "response": {
            "game_count": 49,
            "games": [
                {
                    "appid": 219990,
                    "name": "Grim Dawn",
                    "playtime_forever": 1534,
                    "img_logo_url": "8021ad6119b367593f1b1536aafd11397fb24ae9",
                    "playtime_windows_forever": 1,
                    "playtime_mac_forever": 0,
                    "playtime_linux_forever": 1533,
                    "img_icon_url": "762057f2b14463ae1cbf0701a4cdb25cf94e8a0c",
                    "has_community_visible_stats": True,
                    "rtime_last_played": 0,
                    "content_descriptorids": [],
                    "has_leaderboards": False,
                },
                {
                    "appid": 637650,
                    "name": "FINAL FANTASY XV WINDOWS EDITION",
                    "playtime_forever": 20162,
                    "img_logo_url": "fb3a73c1b6a8305b5dc19110d14420d835956bc0",
                    "playtime_windows_forever": 1,
                    "playtime_mac_forever": 0,
                    "playtime_linux_forever": 20161,
                    "img_icon_url": "0a99fcc7b08c7240d9146390cf1be28451aeef73",
                    "has_community_visible_stats": True,
                    "rtime_last_played": 0,
                    "content_descriptorids": [],
                    "has_leaderboards": False,
                },
            ],
        }
    }


def profile_raw_data() -> dict:
    return {"response": {**player_data()["response"], **player_data()["response"], **summary_data()["response"]}}


def profile_data() -> Profile:
    return Profile(
        player=Player(**summary_data()["response"]["players"][0]),
        games=[Game(**game) for game in player_data()["response"]["games"]],
    )


def game_stats_data() -> dict:
    return {
        "game": {
            "gameName": "Rise of the Tomb Raider",
            "gameVersion": "75",
            "availableGameStats": {
                "stats": [
                    {"name": "EquipmentCrafted", "defaultvalue": 0, "displayName": "Equipment Crafted"},
                    {"name": "ChallengeTombsCompleted", "defaultvalue": 0, "displayName": "Challenge Tombs Completed"},
                ],
                "achievements": [
                    {
                        "name": "NEW_ACHIEVEMENT_3_1",
                        "defaultvalue": 0,
                        "displayName": "Bar Brawl",
                        "hidden": 0,
                        "description": "Melee kill an enemy using a bottle",
                        "icon": "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/391220"
                        "/5cb2c2984f03fc1acd72126741b4141ebbc239f1.jpg",
                        "icongray": "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/391220"
                        "/753ca3075e7fec8d6d339335bacd6681980977ce.jpg",
                    },
                    {
                        "name": "NEW_ACHIEVEMENT_3_2",
                        "defaultvalue": 0,
                        "displayName": "Blade of Justice",
                        "hidden": 0,
                        "description": "Perform 25 special stealth kills with the knife",
                        "icon": "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/391220"
                        "/918bba7906d55ceff7179ded663d499a4fcf6c84.jpg",
                        "icongray": "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/391220"
                        "/a26ad571230e938f5fdc912729bb3f0b309894b6.jpg",
                    },
                ],
            },
        }
    }


def player_stats_data() -> dict:
    return {
        "playerstats": {
            "steamID": "76561198109613067",
            "gameName": "Rise of the Tomb Raider",
            "achievements": [
                {"apiname": "NEW_ACHIEVEMENT_3_1", "achieved": 1, "unlocktime": 1546695765},
                {"apiname": "NEW_ACHIEVEMENT_3_2", "achieved": 1, "unlocktime": 1546342474},
            ],
            "success": True,
        }
    }


def achievement_raw_data() -> dict:
    return {**game_stats_data(), **player_stats_data()}


def achievement_data() -> GameProgress:
    return GameProgress(
        name="Rise of the Tomb Raider",
        achievements=[
            Achievement(
                id="NEW_ACHIEVEMENT_3_1",
                name="Bar Brawl",
                icon="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/391220/5cb2c2984f03fc1acd72126741b4141ebbc239f1.jpg",
                hidden=False,
                achieved=True,
                description="Melee kill an enemy using a bottle",
            ),
            Achievement(
                id="NEW_ACHIEVEMENT_3_2",
                name="Blade of Justice",
                icon="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/391220/918bba7906d55ceff7179ded663d499a4fcf6c84.jpg",
                hidden=False,
                achieved=True,
                description="Perform 25 special stealth kills with the knife",
            ),
        ],
    )
