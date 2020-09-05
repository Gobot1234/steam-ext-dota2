# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: dota_gcmessages_client_team.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto


class ETeamInviteResult(betterproto.Enum):
    Success = 0
    FailureInviteRejected = 1
    FailureInviteTimeout = 2
    ErrorTeamAtMemberLimit = 3
    ErrorTeamLocked = 4
    ErrorInviteeNotAvailable = 5
    ErrorInviteeBusy = 6
    ErrorInviteeAlreadyMember = 7
    ErrorInviteeAtTeamLimit = 8
    ErrorInviteeInsufficientPlayTime = 9
    ErrorInviterInvalidAccountType = 10
    ErrorInviterNotAdmin = 11
    ErrorIncorrectUserResponded = 12
    ErrorUnspecified = 13


class CMsgDOTACreateTeamResponseResult(betterproto.Enum):
    Invalid = -1
    Success = 0
    NameEmpty = 1
    NameBadCharacters = 2
    NameTaken = 3
    NameTooLong = 4
    TagEmpty = 5
    TagBadCharacters = 6
    TagTaken = 7
    TagTooLong = 8
    CreatorBusy = 9
    UnspecifiedError = 10
    CreatorTeamLimitReached = 11
    NoLogo = 12
    CreatorTeamCreationCooldown = 13
    LogoUploadFailed = 14
    NameChangedTooRecently = 15
    CreatorInsufficientLevel = 16
    InvalidAccountType = 17


class CMsgDOTAEditTeamDetailsResponseResult(betterproto.Enum):
    Success = 0
    FailureInvalidAccountType = 1
    FailureNotMember = 2
    FailureTeamLocked = 3
    FailureUnspecifiedError = 4


class CMsgDOTAKickTeamMemberResponseResult(betterproto.Enum):
    Success = 0
    FailureInvalidAccountType = 1
    FailureKickerNotAdmin = 2
    FailureKickeeNotMember = 3
    FailureTeamLocked = 4
    FailureUnspecifiedError = 5


class CMsgDOTATransferTeamAdminResponseResult(betterproto.Enum):
    Success = 0
    FailureInvalidAccountType = 1
    FailureNotAdmin = 2
    FailureSameAccount = 3
    FailureNotMember = 4
    FailureUnspecifiedError = 5


class CMsgDOTALeaveTeamResponseResult(betterproto.Enum):
    Success = 0
    FailureNotMember = 1
    FailureTeamLocked = 2
    FailureUnspecifiedError = 3


@dataclass
class CMsgDOTATeamMemberSDO(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    team_ids: List[int] = betterproto.uint32_field(2)
    profile_team_id: int = betterproto.uint32_field(3)


@dataclass
class CMsgDOTATeamAdminSDO(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    team_ids: List[int] = betterproto.uint32_field(2)


@dataclass
class CMsgDOTATeamMember(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    time_joined: int = betterproto.uint32_field(4)


@dataclass
class CMsgDOTATeam(betterproto.Message):
    members: List["CMsgDOTATeamMember"] = betterproto.message_field(1)
    team_id: int = betterproto.uint32_field(2)
    name: str = betterproto.string_field(3)
    tag: str = betterproto.string_field(4)
    admin_id: int = betterproto.uint32_field(5)
    time_created: int = betterproto.uint32_field(6)
    disbanded: bool = betterproto.bool_field(7)
    wins: int = betterproto.uint32_field(8)
    losses: int = betterproto.uint32_field(9)
    rank: int = betterproto.uint32_field(10)
    calibration_games_remaining: int = betterproto.uint32_field(24)
    logo: int = betterproto.uint64_field(11)
    base_logo: int = betterproto.uint64_field(12)
    banner_logo: int = betterproto.uint64_field(13)
    sponsor_logo: int = betterproto.uint64_field(14)
    country_code: str = betterproto.string_field(15)
    url: str = betterproto.string_field(16)
    fullgamesplayed: int = betterproto.uint32_field(17)
    leagues: List[int] = betterproto.uint32_field(18)
    gamesplayed: int = betterproto.uint32_field(19)
    gamesplayedwithcurrentroster: int = betterproto.uint32_field(20)
    teammatchmakinggamesplayed: int = betterproto.uint32_field(21)
    lastplayedgametime: int = betterproto.uint32_field(22)
    lastrenametime: int = betterproto.uint32_field(23)
    recent_match_ids: List[int] = betterproto.uint64_field(25)
    top_match_ids: List[int] = betterproto.uint64_field(26)
    pickup_team: bool = betterproto.bool_field(27)


@dataclass
class CMsgDOTATeamInfo(betterproto.Message):
    members: List["CMsgDOTATeamInfoMember"] = betterproto.message_field(1)
    team_id: int = betterproto.uint32_field(2)
    name: str = betterproto.string_field(3)
    tag: str = betterproto.string_field(4)
    time_created: int = betterproto.uint32_field(5)
    pro: bool = betterproto.bool_field(6)
    pickup_team: bool = betterproto.bool_field(8)
    ugc_logo: int = betterproto.uint64_field(9)
    ugc_base_logo: int = betterproto.uint64_field(10)
    ugc_banner_logo: int = betterproto.uint64_field(11)
    ugc_sponsor_logo: int = betterproto.uint64_field(12)
    country_code: str = betterproto.string_field(13)
    url: str = betterproto.string_field(14)
    wins: int = betterproto.uint32_field(15)
    losses: int = betterproto.uint32_field(16)
    games_played_total: int = betterproto.uint32_field(19)
    games_played_matchmaking: int = betterproto.uint32_field(20)
    registered_member_account_ids: List[int] = betterproto.uint32_field(30)
    audit_entries: List["CMsgDOTATeamInfoAuditEntry"] = betterproto.message_field(31)
    region: "ELeagueRegion" = betterproto.enum_field(29)


@dataclass
class CMsgDOTATeamInfoMember(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    time_joined: int = betterproto.uint32_field(2)
    admin: bool = betterproto.bool_field(3)


@dataclass
class CMsgDOTATeamInfoAuditEntry(betterproto.Message):
    audit_action: int = betterproto.uint32_field(1)
    timestamp: int = betterproto.uint32_field(2)
    account_id: int = betterproto.uint32_field(3)


@dataclass
class CMsgDOTATeamInfoRequest(betterproto.Message):
    result: "CMsgDOTATeamInfo" = betterproto.message_field(1)


@dataclass
class CMsgDOTATeamsInfo(betterproto.Message):
    league_id: int = betterproto.uint32_field(1)
    teams: List["CMsgDOTATeamInfo"] = betterproto.message_field(2)


@dataclass
class CMsgDOTAMyTeamInfoRequest(betterproto.Message):
    pass


@dataclass
class CMsgDOTACreateTeam(betterproto.Message):
    name: str = betterproto.string_field(1)
    tag: str = betterproto.string_field(2)
    logo: int = betterproto.uint64_field(3)
    base_logo: int = betterproto.uint64_field(4)
    banner_logo: int = betterproto.uint64_field(5)
    sponsor_logo: int = betterproto.uint64_field(6)
    country_code: str = betterproto.string_field(7)
    url: str = betterproto.string_field(8)
    pickup_team: bool = betterproto.bool_field(9)


@dataclass
class CMsgDOTACreateTeamResponse(betterproto.Message):
    result: "CMsgDOTACreateTeamResponseResult" = betterproto.enum_field(1)
    team_id: int = betterproto.uint32_field(2)


@dataclass
class CMsgDOTAEditTeamDetails(betterproto.Message):
    team_id: int = betterproto.uint32_field(1)
    name: str = betterproto.string_field(2)
    tag: str = betterproto.string_field(3)
    logo: int = betterproto.uint64_field(4)
    base_logo: int = betterproto.uint64_field(5)
    banner_logo: int = betterproto.uint64_field(6)
    sponsor_logo: int = betterproto.uint64_field(7)
    country_code: str = betterproto.string_field(8)
    url: str = betterproto.string_field(9)
    in_use_by_party: bool = betterproto.bool_field(10)


@dataclass
class CMsgDOTAEditTeamDetailsResponse(betterproto.Message):
    result: "CMsgDOTAEditTeamDetailsResponseResult" = betterproto.enum_field(1)


@dataclass
class CMsgDOTATeamProfileResponse(betterproto.Message):
    eresult: int = betterproto.uint32_field(1)
    team: "CMsgDOTATeam" = betterproto.message_field(2)


@dataclass
class CMsgDOTAProTeamListRequest(betterproto.Message):
    pass


@dataclass
class CMsgDOTAProTeamListResponse(betterproto.Message):
    teams: List["CMsgDOTAProTeamListResponseTeamEntry"] = betterproto.message_field(1)
    eresult: int = betterproto.uint32_field(2)


@dataclass
class CMsgDOTAProTeamListResponseTeamEntry(betterproto.Message):
    team_id: int = betterproto.uint32_field(1)
    tag: str = betterproto.string_field(2)
    time_created: int = betterproto.uint32_field(3)
    logo: int = betterproto.uint64_field(4)
    country_code: str = betterproto.string_field(5)
    member_count: int = betterproto.uint32_field(6)


@dataclass
class CMsgDOTATeamInviteInviterToGC(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    team_id: int = betterproto.uint32_field(2)


@dataclass
class CMsgDOTATeamInviteGCImmediateResponseToInviter(betterproto.Message):
    result: "ETeamInviteResult" = betterproto.enum_field(1)
    invitee_name: str = betterproto.string_field(2)
    required_play_time: int = betterproto.uint32_field(3)


@dataclass
class CMsgDOTATeamInviteGCRequestToInvitee(betterproto.Message):
    inviter_account_id: int = betterproto.uint32_field(1)
    team_name: str = betterproto.string_field(2)
    team_tag: str = betterproto.string_field(3)
    logo: int = betterproto.uint64_field(4)


@dataclass
class CMsgDOTATeamInviteInviteeResponseToGC(betterproto.Message):
    result: "ETeamInviteResult" = betterproto.enum_field(1)


@dataclass
class CMsgDOTATeamInviteGCResponseToInviter(betterproto.Message):
    result: "ETeamInviteResult" = betterproto.enum_field(1)
    invitee_name: str = betterproto.string_field(2)


@dataclass
class CMsgDOTATeamInviteGCResponseToInvitee(betterproto.Message):
    result: "ETeamInviteResult" = betterproto.enum_field(1)
    team_name: str = betterproto.string_field(2)


@dataclass
class CMsgDOTAKickTeamMember(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    team_id: int = betterproto.uint32_field(2)


@dataclass
class CMsgDOTAKickTeamMemberResponse(betterproto.Message):
    result: "CMsgDOTAKickTeamMemberResponseResult" = betterproto.enum_field(1)


@dataclass
class CMsgDOTATransferTeamAdmin(betterproto.Message):
    new_admin_account_id: int = betterproto.uint32_field(1)
    team_id: int = betterproto.uint32_field(2)


@dataclass
class CMsgDOTATransferTeamAdminResponse(betterproto.Message):
    result: "CMsgDOTATransferTeamAdminResponseResult" = betterproto.enum_field(1)


@dataclass
class CMsgDOTALeaveTeam(betterproto.Message):
    team_id: int = betterproto.uint32_field(1)


@dataclass
class CMsgDOTALeaveTeamResponse(betterproto.Message):
    result: "CMsgDOTALeaveTeamResponseResult" = betterproto.enum_field(1)


@dataclass
class CMsgDOTABetaParticipation(betterproto.Message):
    access_rights: int = betterproto.uint32_field(1)