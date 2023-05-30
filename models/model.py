__strict__ = True

from dataclasses import dataclass
from typing import List


@dataclass
class Player:
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


@dataclass
class Game:
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


@dataclass
class Profile:
    player: Player
    games: List[Game]


@dataclass
class GameAchievement:
    name: str
    displayName: str
    hidden: int
    icon: str
    defaultvalue: int
    icongray: str
    description: str = None


@dataclass
class PlayerAchievement:
    apiname: str
    achieved: int
    unlocktime: int


@dataclass
class PlayerStats:
    steamID: str
    gameName: str
    achievements: List[PlayerAchievement]
    success: bool


@dataclass
class Achievement:
    id: str
    name: str
    icon: str
    hidden: bool
    achieved: bool
    description: str = None


@dataclass
class GameProgress:
    name: str
    achievements: List[Achievement]
