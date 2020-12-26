# -*- coding: utf-8 -*-

from __future__ import annotations

import asyncio
import logging
from typing import Optional, TYPE_CHECKING

from steam import utils
from steam.models import EventParser, register
from steam.state import ConnectionState
from steam.protobufs import GCMsg, GCMsgProto, MsgProto, EMsg
from .enums import Language

if TYPE_CHECKING:
    from .client import Client
    from steam.protobufs.steammessages_clientserver_2 import CMsgGcClient

log = logging.getLogger(__name__)


class GCState(ConnectionState):
    gc_parsers: dict[Language, EventParser] = {}
    client: Client

    def __init__(self, client: Client, **kwargs):
        super().__init__(client, **kwargs)
        self._connected = asyncio.Event()

    @register(EMsg.ClientFromGC)
    async def parse_gc_message(self, msg: MsgProto[CMsgGcClient]) -> None:
        if msg.body.appid != self.client.GAME.id:
            return

        try:
            language = Language(utils.clear_proto_bit(msg.body.msgtype))
        except ValueError:
            return log.info(
                f"Ignoring unknown msg type: {msg.body.msgtype} ({utils.clear_proto_bit(msg.body.msgtype)})"
            )

        try:
            msg = (
                GCMsgProto(language, msg.body.payload)
                if utils.is_proto(msg.body.msgtype)
                else GCMsg(language, msg.body.payload)
            )
        except Exception as exc:
            return log.error(f"Failed to deserialize message: {language!r}, {msg.body.payload!r}", exc_info=exc)
        else:
            if log.isEnabledFor(logging.DEBUG):
                log.debug(f"Socket has received GC message {msg!r} from the websocket.")

        try:
            func = self.gc_parsers[language]
        except KeyError:
            if log.isEnabledFor(logging.DEBUG):
                log.debug(f"Ignoring event {msg!r}")
        else:
            await utils.maybe_coroutine(func, msg)

    @register(Language.ClientWelcome)
    def parse_gc_client_connect(self, _) -> None:
        if not self._connected.is_set():
            self.dispatch("gc_connect")
            self._connected.set()

    def parse_client_goodbye(self, _=None) -> None:
        self.dispatch("gc_disconnect")
        self._connected.clear()

    # TODO impl https://github.com/ValvePython/dota2
