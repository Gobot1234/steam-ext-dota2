# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: dota_gcmessages_client_watch.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto


class CMsgSpectateFriendGameResponseEWatchLiveResult(betterproto.Enum):
    Success = 0
    ErrorGeneric = 1
    ErrorNoPlus = 2
    ErrorNotFriends = 3
    ErrorLobbyNotFound = 4
    ErrorSpectatorInALobby = 5
    ErrorLobbyIsLan = 6
    ErrorWrongLobbyType = 7
    ErrorWrongLobbyState = 8
    ErrorPlayerNotPlayer = 9
    ErrorTooManySpectators = 10
    ErrorSpectatorSwitchedTeams = 11
    ErrorFriendsOnBothSides = 12
    ErrorSpectatorInThisLobby = 13


class CMsgWatchGameResponseWatchGameResult(betterproto.Enum):
    Pending = 0
    Ready = 1
    GameserverNotFound = 2
    Unavailable = 3
    Cancelled = 4
    IncompatibleVersion = 5
    MissingLeagueSubscription = 6
    LobbyNotFound = 7


@dataclass
class CSourceTVGameSmall(betterproto.Message):
    activate_time: int = betterproto.uint32_field(1)
    deactivate_time: int = betterproto.uint32_field(2)
    server_steam_id: int = betterproto.uint64_field(3)
    lobby_id: int = betterproto.uint64_field(4)
    league_id: int = betterproto.uint32_field(5)
    lobby_type: int = betterproto.uint32_field(6)
    game_time: int = betterproto.int32_field(7)
    delay: int = betterproto.uint32_field(8)
    spectators: int = betterproto.uint32_field(9)
    game_mode: int = betterproto.uint32_field(10)
    average_mmr: int = betterproto.uint32_field(11)
    match_id: int = betterproto.uint64_field(12)
    series_id: int = betterproto.uint32_field(13)
    team_name_radiant: str = betterproto.string_field(15)
    team_name_dire: str = betterproto.string_field(16)
    team_logo_radiant: float = betterproto.fixed64_field(24)
    team_logo_dire: float = betterproto.fixed64_field(25)
    team_id_radiant: int = betterproto.uint32_field(30)
    team_id_dire: int = betterproto.uint32_field(31)
    sort_score: int = betterproto.uint32_field(17)
    last_update_time: float = betterproto.float_field(18)
    radiant_lead: int = betterproto.int32_field(19)
    radiant_score: int = betterproto.uint32_field(20)
    dire_score: int = betterproto.uint32_field(21)
    players: List["CSourceTVGameSmallPlayer"] = betterproto.message_field(22)
    building_state: float = betterproto.fixed32_field(23)
    weekend_tourney_tournament_id: int = betterproto.uint32_field(26)
    weekend_tourney_division: int = betterproto.uint32_field(27)
    weekend_tourney_skill_level: int = betterproto.uint32_field(28)
    weekend_tourney_bracket_round: int = betterproto.uint32_field(29)
    custom_game_difficulty: int = betterproto.uint32_field(32)


@dataclass
class CSourceTVGameSmallPlayer(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    hero_id: int = betterproto.uint32_field(2)


@dataclass
class CMsgClientToGCFindTopSourceTVGames(betterproto.Message):
    search_key: str = betterproto.string_field(1)
    league_id: int = betterproto.uint32_field(2)
    hero_id: int = betterproto.uint32_field(3)
    start_game: int = betterproto.uint32_field(4)
    game_list_index: int = betterproto.uint32_field(5)
    lobby_ids: List[int] = betterproto.uint64_field(6)


@dataclass
class CMsgGCToClientFindTopSourceTVGamesResponse(betterproto.Message):
    search_key: str = betterproto.string_field(1)
    league_id: int = betterproto.uint32_field(2)
    hero_id: int = betterproto.uint32_field(3)
    start_game: int = betterproto.uint32_field(4)
    num_games: int = betterproto.uint32_field(5)
    game_list_index: int = betterproto.uint32_field(6)
    game_list: List["CSourceTVGameSmall"] = betterproto.message_field(7)
    specific_games: bool = betterproto.bool_field(8)
    bot_game: "CSourceTVGameSmall" = betterproto.message_field(9)


@dataclass
class CMsgGCToClientTopWeekendTourneyGames(betterproto.Message):
    live_games: List["CSourceTVGameSmall"] = betterproto.message_field(1)


@dataclass
class CMsgClientToGCTopMatchesRequest(betterproto.Message):
    hero_id: int = betterproto.uint32_field(1)
    player_account_id: int = betterproto.uint32_field(2)
    team_id: int = betterproto.uint32_field(3)


@dataclass
class CMsgClientToGCTopLeagueMatchesRequest(betterproto.Message):
    pass


@dataclass
class CMsgClientToGCTopFriendMatchesRequest(betterproto.Message):
    pass


@dataclass
class CMsgClientToGCMatchesMinimalRequest(betterproto.Message):
    match_ids: List[int] = betterproto.uint64_field(1)


@dataclass
class CMsgClientToGCMatchesMinimalResponse(betterproto.Message):
    matches: List["CMsgDOTAMatchMinimal"] = betterproto.message_field(1)
    last_match: bool = betterproto.bool_field(2)


@dataclass
class CMsgGCToClientTopLeagueMatchesResponse(betterproto.Message):
    matches: List["CMsgDOTAMatchMinimal"] = betterproto.message_field(2)


@dataclass
class CMsgGCToClientTopFriendMatchesResponse(betterproto.Message):
    matches: List["CMsgDOTAMatchMinimal"] = betterproto.message_field(1)


@dataclass
class CMsgClientToGCFindTopMatches(betterproto.Message):
    start_game: int = betterproto.uint32_field(1)
    league_id: int = betterproto.uint32_field(2)
    hero_id: int = betterproto.uint32_field(3)
    friend_id: int = betterproto.uint32_field(4)
    friend_list: bool = betterproto.bool_field(5)
    league_list: bool = betterproto.bool_field(6)


@dataclass
class CMsgGCToClientFindTopLeagueMatchesResponse(betterproto.Message):
    start_game: int = betterproto.uint32_field(1)
    league_id: int = betterproto.uint32_field(2)
    hero_id: int = betterproto.uint32_field(3)
    match_ids: List[int] = betterproto.uint32_field(4)
    matches: List["CMsgDOTAMatch"] = betterproto.message_field(5)


@dataclass
class CMsgSpectateFriendGame(betterproto.Message):
    steam_id: float = betterproto.fixed64_field(1)
    live: bool = betterproto.bool_field(2)


@dataclass
class CMsgSpectateFriendGameResponse(betterproto.Message):
    server_steamid: float = betterproto.fixed64_field(4)
    watch_live_result: "CMsgSpectateFriendGameResponseEWatchLiveResult" = betterproto.enum_field(5)


@dataclass
class CDOTAReplayDownloadInfo(betterproto.Message):
    match: "CMsgDOTAMatchMinimal" = betterproto.message_field(1)
    title: str = betterproto.string_field(2)
    description: str = betterproto.string_field(3)
    size: int = betterproto.uint32_field(4)
    tags: List[str] = betterproto.string_field(5)
    exists_on_disk: bool = betterproto.bool_field(6)


@dataclass
class CDOTAReplayDownloadInfoHighlight(betterproto.Message):
    timestamp: int = betterproto.uint32_field(1)
    description: str = betterproto.string_field(2)


@dataclass
class CMsgWatchGame(betterproto.Message):
    server_steamid: float = betterproto.fixed64_field(1)
    client_version: int = betterproto.uint32_field(2)
    watch_server_steamid: float = betterproto.fixed64_field(3)
    lobby_id: int = betterproto.uint64_field(4)
    regions: List[int] = betterproto.uint32_field(5)


@dataclass
class CMsgCancelWatchGame(betterproto.Message):
    pass


@dataclass
class CMsgWatchGameResponse(betterproto.Message):
    watch_game_result: "CMsgWatchGameResponseWatchGameResult" = betterproto.enum_field(1)
    source_tv_public_addr: int = betterproto.uint32_field(2)
    source_tv_private_addr: int = betterproto.uint32_field(3)
    source_tv_port: int = betterproto.uint32_field(4)
    game_server_steamid: float = betterproto.fixed64_field(5)
    watch_server_steamid: float = betterproto.fixed64_field(6)
    watch_tv_unique_secret_code: float = betterproto.fixed64_field(7)


@dataclass
class CMsgPartyLeaderWatchGamePrompt(betterproto.Message):
    game_server_steamid: float = betterproto.fixed64_field(5)


@dataclass
class CDOTABroadcasterInfo(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    server_steam_id: float = betterproto.fixed64_field(2)
    live: bool = betterproto.bool_field(3)
    team_name_radiant: str = betterproto.string_field(4)
    team_name_dire: str = betterproto.string_field(5)
    series_game: int = betterproto.uint32_field(7)
    upcoming_broadcast_timestamp: int = betterproto.uint32_field(9)
    allow_live_video: bool = betterproto.bool_field(10)
    node_type: int = betterproto.uint32_field(11)
    node_name: str = betterproto.string_field(12)


@dataclass
class CMsgDOTASeries(betterproto.Message):
    series_id: int = betterproto.uint32_field(1)
    series_type: int = betterproto.uint32_field(2)
    team_1: "CMsgDOTASeriesTeamInfo" = betterproto.message_field(3)
    team_2: "CMsgDOTASeriesTeamInfo" = betterproto.message_field(4)
    match_minimal: List["CMsgDOTAMatchMinimal"] = betterproto.message_field(5)
    live_game: "CMsgDOTASeriesLiveGame" = betterproto.message_field(6)


@dataclass
class CMsgDOTASeriesTeamInfo(betterproto.Message):
    team_id: int = betterproto.uint32_field(1)
    team_name: str = betterproto.string_field(2)
    team_logo_url: str = betterproto.string_field(3)
    wager_count: int = betterproto.uint32_field(4)


@dataclass
class CMsgDOTASeriesLiveGame(betterproto.Message):
    server_steam_id: float = betterproto.fixed64_field(1)
    team_radiant: "CMsgDOTASeriesTeamInfo" = betterproto.message_field(2)
    team_dire: "CMsgDOTASeriesTeamInfo" = betterproto.message_field(3)
    team_radiant_score: int = betterproto.uint32_field(4)
    team_dire_score: int = betterproto.uint32_field(5)