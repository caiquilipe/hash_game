from dataclasses import dataclass
from constants import EventsEnum
from typing import Union
from schemas.events.on_error import OnError


@dataclass
class Send:
    data: Union["OnError", "OnError"]
    event: EventsEnum

    def __get_data_class(self, event: EventsEnum):
        classes = {EventsEnum.ON_ERROR: OnError}
        return classes[event]

    def __post_init__(self):
        if isinstance(self.data, dict):
            self.data = self.__get_data_class(self.event)(**self.data)

    def send(self):
        return {
            "data": self.data.__dict__,
            "event": self.event.value,
        }
