# -*- coding: utf-8 -*-

from __future__ import annotations

import asyncio
import logging
from typing import Optional, TYPE_CHECKING

from steam import utils
from steam.models import EventParser, register
from steam.state import ConnectionState
from steam.protobufs import GCMsg, GCMsgProto, MsgProto, EMsg

from .channel import Channel
from .enums import Language

from .protobufs import (
    base_gcmessages as cso,
    gcsdk_gcmessages as so,
    dota_gcmessages_client as gc_client,
    econ_gcmessages as econ,
    dota_gcmessages_client_chat as client_chat
)

if TYPE_CHECKING:
    from .client import Client
    from steam.protobufs.steammessages_clientserver_2 import CMsgGcClient

log = logging.getLogger(__name__)


class GCState(ConnectionState):
    gc_parsers: dict[Language, EventParser]
    client: Client

    def __init__(self, client: Client, **kwargs):
        super().__init__(client, **kwargs)
        self._connected = asyncio.Event()

        self._dota_channels: dict[int, Channel] = {}

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
    def parse_gc_client_connect(self, msg: GCMsgProto[gc_client.CMsgDotaWelcome]) -> None:
        if not self._connected.is_set():
            self.dispatch("gc_connect")
            self._connected.set()

        for msg in msg.body.extra_messages:
            msg = MsgProto(EMsg.CMsgGCClient, appid=570, msgtype=utils.set_proto_bit(msg.id), payload=msg.contents)
            await self.parse_gc_message(msg)

        await self.ws.send_gc_message(GCMsgProto(Language.RequestChatChannelList))

    @register(Language.ClientConnectionStatus)
    def parse_goodbye(self, msg: Optional[GCMsgProto[so.CMsgConnectionStatus]] = None) -> None:
        if msg is None or msg.body.status != so.CMsgConnectionStatus.HaveSession:
            self.dispatch("gc_disconnect")
            self._connected.clear()

    @register(Language.RequestChatChannelListResponse)
    async def parse_channels(self, msg: GCMsgProto[client_chat.CMsgDotaRequestChatChannelListResponse]):
        for channel in msg.body.channels:
            await self.ws.send_gc_message(
                GCMsgProto(Language.JoinChatChannel, channel_name=channel.name, channel_type=channel.type)
            )

    @register(Language.JoinChatChannelResponse)
    async def parse_join_channel(self, msg: GCMsgProto[client_chat.CMsgDotaJoinChatChannelResponse]):
        self._dota_channels[msg.body.channel_id] = Channel(self, msg.body)

    async def send_dota_channel_message(self, channel_id: int, content: str):
        await self.ws.send_gc_message(GCMsgProto(Language.GCChatMessage, channel_id=channel_id, text=content))

    async def leave_dota_channel(self, channel_id: int):
        await self.ws.send_gc_message(GCMsgProto(Language.LeaveChatChannel, channel_id=channel_id))
