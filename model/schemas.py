from dataclasses import dataclass
from enum import Enum
from os import uname_result
from uuid import UUID
from datetime import datetime


@dataclass(frozen=True)
class processinfo:
    pid: int
    ppid: int
    name: str
    exe: str
    create_time: datetime
    terminal: str | None
    cmdline: list[str]
    uids: tuple[int, int, int]
    username: str
    cwd: str | None
    # For proces enrichment
    # hash_exe: str | None
    # signature: str | None  # optional


@dataclass(frozen=True)
class networkinfo:
    pass


@dataclass(frozen=True)
class agent_info:
    id: str
    version: float
    OSsysname: str
    hostname: str
    OSrelease: str
    OSVersion: str
    hostId: int


class EventType(str, Enum):
    PROCESS_START = "process_start"
    PROCESS_EXIT = "process_exit"
    NET_CONN = "net_conn"
    DNS_QUERY = "dns_query"
    HEARTBEAT = "heartbeat"
    ETC = "etc"


@dataclass(frozen=True)
class EventModel:
    event_id: str
    event_type: EventType
    timestamp: datetime
    process: processinfo | None
    network: networkinfo | None
    agent_info: agent_info

    # Check logic for Event Schema, (example: if event_type is X then do Y)
    def __post_init__(self):
        if self.timestamp.tzinfo is None:
            raise ValueError("timestamp must be timezone aware")
