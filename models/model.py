__strict__ = True

from dataclasses import dataclass


@dataclass
class Profile:
    steam_id: str
    persona_name: str
    avatar: str
    url: str
    real_name: str
    country_code: str
    games: list


@dataclass
class Game:
    id: int
    name: str
    played: int
    logo: str


@dataclass
class Achievement:
    id: str
    name: str
    description: str
    icon: str
    hidden: bool
    achieved: bool


@dataclass
class GameProgress:
    name: str
    achievements: list
