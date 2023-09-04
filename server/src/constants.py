from enum import Enum


class EventsEnum(str, Enum):
    ON_ERROR = "on_error"
    ON_GAME = "on_game_start"
    ON_USER_CHANGE = "on_user_change"
    ON_HISTORY = "on_history"


class CommandsEnum(str, Enum):
    JOIN_LOBBY_BOT = "join_lobby_bot"
    JOIN_LOBBY = "join_lobby"
    LEAVE_LOBBY = "leave_lobby"
    READY = "ready"
    UNREADY = "unready"
    START_GAME = "start_game"
    PLAY_GAME = "play_game"
    HISTORY = "history"


class PlayerStatusEnum(str, Enum):
    WAITING = "waiting"
    IDLE = "idle"
    READY = "ready"
    PLAYING = "playing"
    YOUR_TURN = "your_turn"
    ADVERSARY = "adversary"
    WINNER = "winner"
    LOSER = "loser"
