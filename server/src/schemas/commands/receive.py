from dataclasses import dataclass
from typing import Union
from constants import CommandsEnum
from schemas.commands.join_lobby import JoinLobby


@dataclass
class Receive:
    data: Union["JoinLobby", "JoinLobby"]
    command: CommandsEnum

    def __get_data_class(self, command: CommandsEnum):
        classes = {CommandsEnum.JOIN_LOBBY: JoinLobby}
        return classes[command]

    def __post_init__(self):
        if isinstance(self.data, dict):
            self.data = self.__get_data_class(self.command)(**self.data)

    def send(self):
        return self.data.__dict__
