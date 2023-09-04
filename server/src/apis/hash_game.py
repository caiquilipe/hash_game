from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from constants import EventsEnum
from schemas.events.on_error import OnError
from repositories.websocket_repository import WebsocketRepository
import logging
import asyncio

logger = logging.getLogger(__name__)


class APIHashGame(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_routes()

    def _set_routes(self):
        self.add_api_websocket_route(
            path="/ws/{username}",
            endpoint=self.websocket,
            name="websocket",
        )

    async def websocket(self, websocket: WebSocket, username: str):
        self.__websocket_repository = WebsocketRepository(websocket)
        await websocket.accept()
        try:
            while True:
                await self.__websocket_repository.receive_command()
        except Exception as e:
            await self.__handle_error(websocket, e)
        finally:
            await websocket.close()

    async def __handle_error(self, error: Exception):
        if isinstance(error, WebSocketDisconnect):
            logger.warning("Websocket connection closed")
        else:
            logger.error(f"Websocket error: {error}")
            data = OnError(message=str(error))
            event = EventsEnum.ON_ERROR
            await self.__websocket_repository.send_event(data, event)
            await asyncio.sleep(2)
