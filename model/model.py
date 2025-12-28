import os
import socket
from datetime import datetime
import psutil
from enum import Enum
from collections.abc import ItemsView


class testeable:
    def printall(self):
        dict_items: dict[str, str | float] = self.__dict__
        items: ItemsView[str, str | float] = dict_items.items()

        for k, v in items:
            print(f"{str(k)} = {str(v)}")


class EventType(Enum):
    process_start = 1
    process_exit = 2
    net_conn = 3
    dns_query = 4
    heartbeat = 5
    etc = 6


class process:
    def __init__(self, pid: int):
        self.pid: int = pid

        self.ppid: int
        self.name: str
        self.exe_path: str

        self.cmd_line: str
        self.user_uid: int
        self.user_name: str

        self.working_dir: str  # optional

        # For proces enrichment
        self.hash_exe: str
        self.signature: str  # optional

    def process_enrichment(self):
        pass

    def process_snapshot(self):
        pass


class event:
    def __init__(self, id: str, type: str, pid: int):
        self.id: str
        self.type: list[str]
        self.created: datetime = datetime.now()

    def process_telemetry(self):
        pass


class agent(testeable):
    def __init__(self):
        osinfo = os.uname()
        self.id: str = "Agentv1"
        self.version: float = 1.0
        self.OSsysname: str = osinfo[0]
        self.hostname: str = socket.gethostname()
        self.OSrelease: str = osinfo[2]
        self.OSVersion: str = osinfo[3]
        self.hostId: str


class EventModel(agent):
    def __init__(self) -> None:
        super().__init__()

    def iterate_events(self):
        pass


def count_open_connections():
    connections = psutil.net_connections()
    return len(connections)


def p_key(d):
    return (d.get("ppid"), d.get("pid"), d.get("proc_name"))
