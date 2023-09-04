from fastapi import WebSocket
from constants import CommandsEnum

from schemas.commands.receive import Receive
from schemas.events.send import Send
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from schemas.events.on_error import OnError
    from constants import EventsEnum


class WebsocketRepository:
    def __init__(self, websocket: WebSocket):
        self.__websocket = websocket
        self.__commands = {
            CommandsEnum.JOIN_LOBBY_BOT: "",
            CommandsEnum.JOIN_LOBBY: "",
            CommandsEnum.LEAVE_LOBBY: "",
            CommandsEnum.START_GAME: "",
            CommandsEnum.READY: "",
            CommandsEnum.UNREADY: "",
            CommandsEnum.PLAY_GAME: "",
            CommandsEnum.HISTORY: "",
        }

    async def receive_command(self):
        receive = Receive(**await self.__websocket.receive_json())
        self.__commands[receive.command](receive.send())

    async def send_event(self, data: Union["OnError", "OnError"], event: EventsEnum):
        message = Send(data, event)
        await self.__websocket.send_json(message.send())
