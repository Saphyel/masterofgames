__strict__ = True

from typing import List
from pydantic import BaseModel


class Player(BaseModel):
    steamid: str
    profilestate: str
    personaname: str
    lastlogoff: int
    profileurl: str
    avatar: str
    realname: str
    timecreated: int
    loccountrycode: str
    communityvisibilitystate: int
    avatarmedium: str
    avatarfull: str
    avatarhash: str
    personastate: int
    primaryclanid: str
    personastateflags: int
    locstatecode: str



class Game(BaseModel):
    appid: int
    name: str
    playtime_forever: int
    playtime_windows_forever: int
    playtime_mac_forever: int
    playtime_linux_forever: int
    img_icon_url: str
    img_logo_url: str = None
    has_community_visible_stats: bool = None
    playtime_2weeks: int = None
    rtime_last_played: int = None
    content_descriptorids: list = None
    has_leaderboards: bool = None



class Profile(BaseModel):
    player: Player
    games: List[Game]



class GameAchievement(BaseModel):
    name: str
    displayName: str
    hidden: int
    icon: str
    defaultvalue: int
    icongray: str
    description: str = None



class PlayerAchievement(BaseModel):
    apiname: str
    achieved: int
    unlocktime: int



class PlayerStats(BaseModel):
    steamID: str
    gameName: str
    achievements: List[PlayerAchievement]
    success: bool



class Achievement(BaseModel):
    id: str
    name: str
    icon: str
    hidden: bool
    achieved: bool
    description: str = None



class GameProgress(BaseModel):
    name: str
    achievements: List[Achievement]
