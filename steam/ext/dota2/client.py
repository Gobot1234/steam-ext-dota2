# -*- coding: utf-8 -*-

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Optional, Any

from typing_extensions import Final

from steam import DOTA2, Client, Game
from steam.ext import commands

from .state import GCState


__all__ = (
    "Client",
    "Bot",
)


class Client(Client):
    GAME: Final[Game] = DOTA2

    def __init__(self, **options: Any):
        game = options.pop("game", None)
        if game is not None:  # don't let them overwrite the main game
            try:
                options["games"].append(game)
            except (TypeError, KeyError):
                options["games"] = [game]
        options["game"] = DOTA2
        super().__init__(**options)
        self._connection = GCState(client=self, **options)
        self._gc_connect_task: Optional[asyncio.Task] = None

    # boring subclass stuff

    """
    async def start(self, *args, **kwargs) -> None:
        self._gc_connect_task = self.loop.create_task(self._on_gc_connect())
        await super().start(*args, **kwargs)

    async def _on_gc_connect(self) -> None:
        await self.wait_until_ready()
        self._connection._unpatched_inventory = self.user.inventory
        await self.wait_for("gc_connect")
        while True:  # this is ok-ish as gateway.KeepAliveHandler should catch any blocking and disconnects
            await self.ws.send_gc_message(GCMsg(Language.ClientHello))
            await asyncio.sleep(5)

    async def close(self) -> None:
        await self.ws.send_gc_message(GCMsg(Language.ClientGoodbye))
        self._gc_connect_task.cancel()
        await super().close()
        """

    if TYPE_CHECKING:

        async def on_gc_connect(self) -> None:
            """|coro|
            Called after the client receives the welcome message from the  GC.
            """

        async def on_gc_disconnect(self) -> None:
            """|coro|
            Called after the client receives the goodbye message from the  GC.
            """

        async def on_gc_ready(self) -> None:
            """|coro|
            Called after the client connects to the GC.
            """


class Bot(commands.Bot, Client):
    pass
