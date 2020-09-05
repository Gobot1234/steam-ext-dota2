# -*- coding: utf-8 -*-

import asyncio
import logging
from typing import Awaitable, Callable, Dict, Optional, TYPE_CHECKING

import steam
from steam.state import ConnectionState, register as register_emsg
from steam.protobufs import MsgProto, EMsg

if TYPE_CHECKING:
    from steam import Client, IntEnum
    from steam.http import HTTPClient

log = logging.getLogger(__name__)
Default = MsgProto["CMsgGcClient"]
EventParser = Callable[["GCState", Default], Optional[Awaitable[None]]]


class Registerer:
    __slots__ = ("func", "enum")

    def __init__(self, func: EventParser, enum: "IntEnum"):
        self.func = func
        self.enum = enum

    def __set_name__(self, state: "GCState", _):
        state.gc_parsers[self.enum] = self.func


def register(enum: "IntEnum") -> Callable[[EventParser], Registerer]:
    def decorator(func: EventParser):
        return Registerer(func, enum)

    return decorator


class GCState(ConnectionState):
    gc_parsers: Dict["IntEnum", EventParser] = dict()

    __slots__ = ("_has_gc_session",)

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        client: "Client",
        http: "HTTPClient",
        **kwargs,
    ):
        super().__init__(loop, client, http, **kwargs)

    @register_emsg(EMsg.ClientFromGC)
    async def parse_gc_message(self, msg: Default):
        if msg.body.appid != steam.DOTA2:
            return
        # event parsing logic
        # get the relevant IntEnum
        try:
            enum = IntEnum(steam.utils.clear_proto_bit(msg.body.msgtype))
        except ValueError:
            return log.info(
                f"Ignoring unknown msg type: {msg.body.msgtype} ({steam.utils.clear_proto_bit(msg.body.msgtype)})"
            )

        try:
            func = self.gc_parsers[enum]
        except KeyError:
            log.debug(f"Ignoring event {msg!r}")
        else:
            await steam.utils.maybe_coroutine(func, self, msg)

    @register(IntEnum.attr)
    def some_function(self, msg: MsgProto):
        # parse it
        # dispatch some event
        pass

    # TODO impl https://github.com/ValvePython/dota2
