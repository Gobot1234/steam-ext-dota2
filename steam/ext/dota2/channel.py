from steam.abc import Messageable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .protobufs.dota_gcmessages_client_chat import CMsgDotaJoinChatChannelResponse
    from .state import GCState


class Channel(Messageable):
    def __init__(self, state: GCState, msg: CMsgDotaJoinChatChannelResponse):
        self._state = state
        self.members = {}
        self.id = msg.channel_id
        self.name = msg.channel_name
        self.type = msg.channel_type
        self.user_id = msg.channel_user_id
        self.max_members = msg.max_members

    def _get_image_endpoint(self):
        raise NotImplementedError("can't send images to a dota channel")

    def _get_message_endpoint(self):
        return self.id, self._state.send_dota_channel_message

    async def leave(self) -> None:
        await self._state.leave_dota_channel(self.id)
