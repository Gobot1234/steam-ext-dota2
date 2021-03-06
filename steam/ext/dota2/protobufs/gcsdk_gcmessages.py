# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: gcsdk_gcmessages.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto


class ESourceEngine(betterproto.Enum):
    Source1 = 0
    Source2 = 1


class PartnerAccountType(betterproto.Enum):
    NONE = 0
    PerfectWorld = 1
    Invalid = 3


class GcConnectionStatus(betterproto.Enum):
    HaveSession = 0
    GcGoingDown = 1
    NoSession = 2
    NoSessionInLogonQueue = 3
    NoSteam = 4
    Suspended = 5
    SteamGoingDown = 6


@dataclass(eq=False, repr=False)
class CgcSystemMsgGetAccountDetailsResponse(betterproto.Message):
    eresult_deprecated: int = betterproto.uint32_field(1)
    account_name: str = betterproto.string_field(2)
    persona_name: str = betterproto.string_field(3)
    is_profile_created: bool = betterproto.bool_field(26)
    is_profile_public: bool = betterproto.bool_field(4)
    is_inventory_public: bool = betterproto.bool_field(5)
    is_vac_banned: bool = betterproto.bool_field(7)
    is_cyber_cafe: bool = betterproto.bool_field(8)
    is_school_account: bool = betterproto.bool_field(9)
    is_limited: bool = betterproto.bool_field(10)
    is_subscribed: bool = betterproto.bool_field(11)
    package: int = betterproto.uint32_field(12)
    is_free_trial_account: bool = betterproto.bool_field(13)
    free_trial_expiration: int = betterproto.uint32_field(14)
    is_low_violence: bool = betterproto.bool_field(15)
    is_account_locked_down: bool = betterproto.bool_field(16)
    is_community_banned: bool = betterproto.bool_field(17)
    is_trade_banned: bool = betterproto.bool_field(18)
    trade_ban_expiration: int = betterproto.uint32_field(19)
    accountid: int = betterproto.uint32_field(20)
    suspension_end_time: int = betterproto.uint32_field(21)
    currency: str = betterproto.string_field(22)
    steam_level: int = betterproto.uint32_field(23)
    friend_count: int = betterproto.uint32_field(24)
    account_creation_time: int = betterproto.uint32_field(25)
    is_steamguard_enabled: bool = betterproto.bool_field(27)
    is_phone_verified: bool = betterproto.bool_field(28)
    is_two_factor_auth_enabled: bool = betterproto.bool_field(29)
    two_factor_enabled_time: int = betterproto.uint32_field(30)
    phone_verification_time: int = betterproto.uint32_field(31)
    phone_id: int = betterproto.uint64_field(33)
    is_phone_identifying: bool = betterproto.bool_field(34)
    rt_identity_linked: int = betterproto.uint32_field(35)
    rt_birth_date: int = betterproto.uint32_field(36)
    txn_country_code: str = betterproto.string_field(37)
    has_accepted_china_ssa: bool = betterproto.bool_field(38)


@dataclass(eq=False, repr=False)
class CMsgGcAssertJobData(betterproto.Message):
    message_type: str = betterproto.string_field(1)
    message_data: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class CMsgGcConCommand(betterproto.Message):
    command: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class CMsgSdoAssert(betterproto.Message):
    sdo_type: int = betterproto.int32_field(1)
    requests: List["CMsgSdoAssertRequest"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class CMsgSdoAssertRequest(betterproto.Message):
    key: List[int] = betterproto.uint64_field(1)
    requesting_job: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class CMsgSha1Digest(betterproto.Message):
    block1: int = betterproto.fixed64_field(1)
    block2: int = betterproto.fixed64_field(2)
    block3: int = betterproto.fixed32_field(3)


@dataclass(eq=False, repr=False)
class CMsgSoidOwner(betterproto.Message):
    type: int = betterproto.uint32_field(1)
    id: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class CMsgSoSingleObject(betterproto.Message):
    type_id: int = betterproto.int32_field(2)
    object_data: bytes = betterproto.bytes_field(3)
    version: int = betterproto.fixed64_field(4)
    owner_soid: "CMsgSoidOwner" = betterproto.message_field(5)
    service_id: int = betterproto.uint32_field(6)


@dataclass(eq=False, repr=False)
class CMsgSoMultipleObjects(betterproto.Message):
    objects_modified: List["CMsgSoMultipleObjectsSingleObject"] = betterproto.message_field(2)
    version: int = betterproto.fixed64_field(3)
    objects_added: List["CMsgSoMultipleObjectsSingleObject"] = betterproto.message_field(4)
    objects_removed: List["CMsgSoMultipleObjectsSingleObject"] = betterproto.message_field(5)
    owner_soid: "CMsgSoidOwner" = betterproto.message_field(6)
    service_id: int = betterproto.uint32_field(7)


@dataclass(eq=False, repr=False)
class CMsgSoMultipleObjectsSingleObject(betterproto.Message):
    type_id: int = betterproto.int32_field(1)
    object_data: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class CMsgSoCacheSubscribed(betterproto.Message):
    objects: List["CMsgSoCacheSubscribedSubscribedType"] = betterproto.message_field(2)
    version: int = betterproto.fixed64_field(3)
    owner_soid: "CMsgSoidOwner" = betterproto.message_field(4)
    service_id: int = betterproto.uint32_field(5)
    service_list: List[int] = betterproto.uint32_field(6)
    sync_version: int = betterproto.fixed64_field(7)


@dataclass(eq=False, repr=False)
class CMsgSoCacheSubscribedSubscribedType(betterproto.Message):
    type_id: int = betterproto.int32_field(1)
    object_data: List[bytes] = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class CMsgSoCacheSubscribedUpToDate(betterproto.Message):
    version: int = betterproto.fixed64_field(1)
    owner_soid: "CMsgSoidOwner" = betterproto.message_field(2)
    service_id: int = betterproto.uint32_field(3)
    service_list: List[int] = betterproto.uint32_field(4)
    sync_version: int = betterproto.fixed64_field(5)


@dataclass(eq=False, repr=False)
class CMsgSoCacheUnsubscribed(betterproto.Message):
    owner_soid: "CMsgSoidOwner" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class CMsgSoCacheSubscriptionCheck(betterproto.Message):
    version: int = betterproto.fixed64_field(2)
    owner_soid: "CMsgSoidOwner" = betterproto.message_field(3)
    service_id: int = betterproto.uint32_field(4)
    service_list: List[int] = betterproto.uint32_field(5)
    sync_version: int = betterproto.fixed64_field(6)


@dataclass(eq=False, repr=False)
class CMsgSoCacheSubscriptionRefresh(betterproto.Message):
    owner_soid: "CMsgSoidOwner" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class CMsgSoCacheVersion(betterproto.Message):
    version: int = betterproto.fixed64_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcMultiplexMessage(betterproto.Message):
    msgtype: int = betterproto.uint32_field(1)
    payload: bytes = betterproto.bytes_field(2)
    steamids: List[int] = betterproto.fixed64_field(3)


@dataclass(eq=False, repr=False)
class CMsgGcToGcSubGcStarting(betterproto.Message):
    dir_index: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class CgcToGcMsgMasterAck(betterproto.Message):
    dir_index: int = betterproto.uint32_field(1)
    machine_name: str = betterproto.string_field(3)
    process_name: str = betterproto.string_field(4)
    directory: List["CgcToGcMsgMasterAckProcess"] = betterproto.message_field(6)


@dataclass(eq=False, repr=False)
class CgcToGcMsgMasterAckProcess(betterproto.Message):
    dir_index: int = betterproto.uint32_field(1)
    type_instances: List[int] = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class CgcToGcMsgMasterAckResponse(betterproto.Message):
    eresult: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcToGcUniverseStartup(betterproto.Message):
    is_initial_startup: bool = betterproto.bool_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcToGcUniverseStartupResponse(betterproto.Message):
    eresult: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class CgcToGcMsgMasterStartupComplete(betterproto.Message):
    gc_info: List["CgcToGcMsgMasterStartupCompleteGcInfo"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class CgcToGcMsgMasterStartupCompleteGcInfo(betterproto.Message):
    dir_index: int = betterproto.uint32_field(1)
    machine_name: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class CgcToGcMsgRouted(betterproto.Message):
    msg_type: int = betterproto.uint32_field(1)
    sender_id: int = betterproto.fixed64_field(2)
    net_message: bytes = betterproto.bytes_field(3)


@dataclass(eq=False, repr=False)
class CgcToGcMsgRoutedReply(betterproto.Message):
    msg_type: int = betterproto.uint32_field(1)
    net_message: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class CMsgGcUpdateSubGcSessionInfo(betterproto.Message):
    updates: List["CMsgGcUpdateSubGcSessionInfoCMsgUpdate"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcUpdateSubGcSessionInfoCMsgUpdate(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    ip: int = betterproto.fixed32_field(2)
    trusted: bool = betterproto.bool_field(3)


@dataclass(eq=False, repr=False)
class CMsgGcRequestSubGcSessionInfo(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcRequestSubGcSessionInfoResponse(betterproto.Message):
    ip: int = betterproto.fixed32_field(1)
    trusted: bool = betterproto.bool_field(2)
    port: int = betterproto.uint32_field(3)
    success: bool = betterproto.bool_field(4)


@dataclass(eq=False, repr=False)
class CMsgSoCacheHaveVersion(betterproto.Message):
    soid: "CMsgSoidOwner" = betterproto.message_field(1)
    version: int = betterproto.fixed64_field(2)
    service_id: int = betterproto.uint32_field(3)
    cached_file_version: int = betterproto.uint32_field(4)


@dataclass(eq=False, repr=False)
class CMsgClientHello(betterproto.Message):
    version: int = betterproto.uint32_field(1)
    socache_have_versions: List["CMsgSoCacheHaveVersion"] = betterproto.message_field(2)
    client_session_need: int = betterproto.uint32_field(3)
    client_launcher: "PartnerAccountType" = betterproto.enum_field(4)
    secret_key: str = betterproto.string_field(5)
    client_language: int = betterproto.uint32_field(6)
    engine: "ESourceEngine" = betterproto.enum_field(7)
    steamdatagram_login: bytes = betterproto.bytes_field(8)
    platform_id: int = betterproto.uint32_field(9)
    game_msg: bytes = betterproto.bytes_field(10)
    os_type: int = betterproto.int32_field(11)
    render_system: int = betterproto.uint32_field(12)
    render_system_req: int = betterproto.uint32_field(13)
    screen_width: int = betterproto.uint32_field(14)
    screen_height: int = betterproto.uint32_field(15)
    screen_refresh: int = betterproto.uint32_field(16)
    render_width: int = betterproto.uint32_field(17)
    render_height: int = betterproto.uint32_field(18)
    swap_width: int = betterproto.uint32_field(19)
    swap_height: int = betterproto.uint32_field(20)
    is_steam_china: bool = betterproto.bool_field(22)
    platform_name: str = betterproto.string_field(23)


@dataclass(eq=False, repr=False)
class CMsgClientWelcome(betterproto.Message):
    version: int = betterproto.uint32_field(1)
    game_data: bytes = betterproto.bytes_field(2)
    outofdate_subscribed_caches: List["CMsgSoCacheSubscribed"] = betterproto.message_field(3)
    uptodate_subscribed_caches: List["CMsgSoCacheSubscriptionCheck"] = betterproto.message_field(4)
    location: "CMsgClientWelcomeLocation" = betterproto.message_field(5)
    save_game_key: bytes = betterproto.bytes_field(6)
    item_schema_crc: int = betterproto.fixed32_field(7)
    items_game_url: str = betterproto.string_field(8)
    gc_socache_file_version: int = betterproto.uint32_field(9)
    txn_country_code: str = betterproto.string_field(10)
    game_data2: bytes = betterproto.bytes_field(11)
    rtime32_gc_welcome_timestamp: int = betterproto.uint32_field(12)
    currency: int = betterproto.uint32_field(13)
    balance: int = betterproto.uint32_field(14)
    balance_url: str = betterproto.string_field(15)
    has_accepted_china_ssa: bool = betterproto.bool_field(16)


@dataclass(eq=False, repr=False)
class CMsgClientWelcomeLocation(betterproto.Message):
    latitude: float = betterproto.float_field(1)
    longitude: float = betterproto.float_field(2)
    country: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class CMsgConnectionStatus(betterproto.Message):
    status: "GcConnectionStatus" = betterproto.enum_field(1)
    client_session_need: int = betterproto.uint32_field(2)
    queue_position: int = betterproto.int32_field(3)
    queue_size: int = betterproto.int32_field(4)
    wait_seconds: int = betterproto.int32_field(5)
    estimated_wait_seconds_remaining: int = betterproto.int32_field(6)


@dataclass(eq=False, repr=False)
class CMsgGcToGcsoCacheSubscribe(betterproto.Message):
    subscriber: int = betterproto.fixed64_field(1)
    subscribe_to_id: int = betterproto.fixed64_field(2)
    sync_version: int = betterproto.fixed64_field(3)
    have_versions: List["CMsgGcToGcsoCacheSubscribeCMsgHaveVersions"] = betterproto.message_field(4)
    subscribe_to_type: int = betterproto.uint32_field(5)


@dataclass(eq=False, repr=False)
class CMsgGcToGcsoCacheSubscribeCMsgHaveVersions(betterproto.Message):
    service_id: int = betterproto.uint32_field(1)
    version: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class CMsgGcToGcsoCacheUnsubscribe(betterproto.Message):
    subscriber: int = betterproto.fixed64_field(1)
    unsubscribe_from_id: int = betterproto.fixed64_field(2)
    unsubscribe_from_type: int = betterproto.uint32_field(3)


@dataclass(eq=False, repr=False)
class CMsgGcClientPing(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class CMsgGcToGcForwardAccountDetails(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    account_details: "CgcSystemMsgGetAccountDetailsResponse" = betterproto.message_field(2)
    age_seconds: int = betterproto.uint32_field(3)


@dataclass(eq=False, repr=False)
class CMsgGcToGcLoadSessionSoCache(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    forward_account_details: "CMsgGcToGcForwardAccountDetails" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class CMsgGcToGcLoadSessionSoCacheResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class CMsgGcToGcUpdateSessionStats(betterproto.Message):
    user_sessions: int = betterproto.uint32_field(1)
    server_sessions: int = betterproto.uint32_field(2)
    in_logon_surge: bool = betterproto.bool_field(3)


@dataclass(eq=False, repr=False)
class CMsgGcToClientRequestDropped(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class CWorkshopPopulateItemDescriptionsRequest(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    languages: List[
        "CWorkshopPopulateItemDescriptionsRequestItemDescriptionsLanguageBlock"
    ] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class CWorkshopPopulateItemDescriptionsRequestSingleItemDescription(betterproto.Message):
    gameitemid: int = betterproto.uint32_field(1)
    item_description: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class CWorkshopPopulateItemDescriptionsRequestItemDescriptionsLanguageBlock(betterproto.Message):
    language: str = betterproto.string_field(1)
    descriptions: List["CWorkshopPopulateItemDescriptionsRequestSingleItemDescription"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class CWorkshopGetContributorsRequest(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    gameitemid: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class CWorkshopGetContributorsResponse(betterproto.Message):
    contributors: List[int] = betterproto.fixed64_field(1)


@dataclass(eq=False, repr=False)
class CWorkshopSetItemPaymentRulesRequest(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    gameitemid: int = betterproto.uint32_field(2)
    associated_workshop_files: List[
        "CWorkshopSetItemPaymentRulesRequestWorkshopItemPaymentRule"
    ] = betterproto.message_field(3)
    partner_accounts: List["CWorkshopSetItemPaymentRulesRequestPartnerItemPaymentRule"] = betterproto.message_field(4)
    validate_only: bool = betterproto.bool_field(5)
    make_workshop_files_subscribable: bool = betterproto.bool_field(6)
    associated_workshop_file_for_direct_payments: "CWorkshopSetItemPaymentRulesRequestWorkshopDirectPaymentRule" = (
        betterproto.message_field(7)
    )


@dataclass(eq=False, repr=False)
class CWorkshopSetItemPaymentRulesRequestWorkshopItemPaymentRule(betterproto.Message):
    workshop_file_id: int = betterproto.uint64_field(1)
    revenue_percentage: float = betterproto.float_field(2)
    rule_description: str = betterproto.string_field(3)
    rule_type: int = betterproto.uint32_field(4)


@dataclass(eq=False, repr=False)
class CWorkshopSetItemPaymentRulesRequestWorkshopDirectPaymentRule(betterproto.Message):
    workshop_file_id: int = betterproto.uint64_field(1)
    rule_description: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class CWorkshopSetItemPaymentRulesRequestPartnerItemPaymentRule(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    revenue_percentage: float = betterproto.float_field(2)
    rule_description: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class CWorkshopSetItemPaymentRulesResponse(betterproto.Message):
    validation_errors: List[str] = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class CCommunityClanAnnouncementInfo(betterproto.Message):
    gid: int = betterproto.uint64_field(1)
    clanid: int = betterproto.uint64_field(2)
    posterid: int = betterproto.uint64_field(3)
    headline: str = betterproto.string_field(4)
    posttime: int = betterproto.uint32_field(5)
    updatetime: int = betterproto.uint32_field(6)
    body: str = betterproto.string_field(7)
    commentcount: int = betterproto.int32_field(8)
    tags: List[str] = betterproto.string_field(9)
    language: int = betterproto.int32_field(10)
    hidden: bool = betterproto.bool_field(11)
    forum_topic_id: int = betterproto.fixed64_field(12)


@dataclass(eq=False, repr=False)
class CCommunityGetClanAnnouncementsRequest(betterproto.Message):
    steamid: int = betterproto.uint64_field(1)
    offset: int = betterproto.uint32_field(2)
    count: int = betterproto.uint32_field(3)
    maxchars: int = betterproto.uint32_field(4)
    strip_html: bool = betterproto.bool_field(5)
    required_tags: List[str] = betterproto.string_field(6)
    require_no_tags: bool = betterproto.bool_field(7)
    language_preference: List[int] = betterproto.uint32_field(8)
    hidden_only: bool = betterproto.bool_field(9)
    only_gid: bool = betterproto.bool_field(10)
    rtime_oldest_date: int = betterproto.uint32_field(11)
    include_hidden: bool = betterproto.bool_field(12)
    include_partner_events: bool = betterproto.bool_field(13)


@dataclass(eq=False, repr=False)
class CCommunityGetClanAnnouncementsResponse(betterproto.Message):
    maxchars: int = betterproto.uint32_field(1)
    strip_html: bool = betterproto.bool_field(2)
    announcements: List["CCommunityClanAnnouncementInfo"] = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class CBroadcastPostGameDataFrameRequest(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    steamid: int = betterproto.fixed64_field(2)
    broadcast_id: int = betterproto.fixed64_field(3)
    frame_data: bytes = betterproto.bytes_field(4)


@dataclass(eq=False, repr=False)
class CMsgSerializedSoCache(betterproto.Message):
    file_version: int = betterproto.uint32_field(1)
    caches: List["CMsgSerializedSoCacheCache"] = betterproto.message_field(2)
    gc_socache_file_version: int = betterproto.uint32_field(3)


@dataclass(eq=False, repr=False)
class CMsgSerializedSoCacheTypeCache(betterproto.Message):
    type: int = betterproto.uint32_field(1)
    objects: List[bytes] = betterproto.bytes_field(2)
    service_id: int = betterproto.uint32_field(3)


@dataclass(eq=False, repr=False)
class CMsgSerializedSoCacheCache(betterproto.Message):
    type: int = betterproto.uint32_field(1)
    id: int = betterproto.uint64_field(2)
    versions: List["CMsgSerializedSoCacheCacheVersion"] = betterproto.message_field(3)
    type_caches: List["CMsgSerializedSoCacheTypeCache"] = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class CMsgSerializedSoCacheCacheVersion(betterproto.Message):
    service: int = betterproto.uint32_field(1)
    version: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class CMsgGcToClientPollConvarRequest(betterproto.Message):
    convar_name: str = betterproto.string_field(1)
    poll_id: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class CMsgGcToClientPollConvarResponse(betterproto.Message):
    poll_id: int = betterproto.uint32_field(1)
    convar_value: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class CgcMsgCompressedMsgToClient(betterproto.Message):
    msg_id: int = betterproto.uint32_field(1)
    compressed_msg: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class CMsgGcToGcMasterBroadcastMessage(betterproto.Message):
    users_per_second: int = betterproto.uint32_field(1)
    send_to_users: bool = betterproto.bool_field(2)
    send_to_servers: bool = betterproto.bool_field(3)
    msg_id: int = betterproto.uint32_field(4)
    msg_data: bytes = betterproto.bytes_field(5)


@dataclass(eq=False, repr=False)
class CMsgGcToGcMasterSubscribeToCache(betterproto.Message):
    soid_type: int = betterproto.uint32_field(1)
    soid_id: int = betterproto.fixed64_field(2)
    account_ids: List[int] = betterproto.uint32_field(3)
    steam_ids: List[int] = betterproto.fixed64_field(4)


@dataclass(eq=False, repr=False)
class CMsgGcToGcMasterSubscribeToCacheResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class CMsgGcToGcMasterSubscribeToCacheAsync(betterproto.Message):
    subscribe_msg: "CMsgGcToGcMasterSubscribeToCache" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcToGcMasterUnsubscribeFromCache(betterproto.Message):
    soid_type: int = betterproto.uint32_field(1)
    soid_id: int = betterproto.fixed64_field(2)
    account_ids: List[int] = betterproto.uint32_field(3)
    steam_ids: List[int] = betterproto.fixed64_field(4)


@dataclass(eq=False, repr=False)
class CMsgGcToGcMasterDestroyCache(betterproto.Message):
    soid_type: int = betterproto.uint32_field(1)
    soid_id: int = betterproto.fixed64_field(2)
