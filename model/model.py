import os
import socket
import psutil

# According to uuid1() getnode() is used to get hardware address aka hostid
from uuid import getnode

from model.schemas import EventModel, processinfo, agent_info
from model.eventfactory import EventFactory

# For test
from collections.abc import ItemsView


class testeable:
    def printall(self):
        dict_items: dict[str, str | float] = self.__dict__
        items: ItemsView[str, str | float] = dict_items.items()

        for k, v in items:
            print(f"{str(k)} = {str(v)}")


class Agent:
    def __init__(self):
        osinfo: os.uname_result = os.uname()
        self.id: str = "Agentv1"
        self.version: float = 1.0
        self.OSsysname: str = osinfo[0]
        self.hostname: str = socket.gethostname()
        self.OSrelease: str = osinfo[2]
        self.OSVersion: str = osinfo[3]
        self.hostId: int = getnode()

    def get_agent_info(self):
        return agent_info(
            id=self.id,
            version=self.version,
            OSsysname=self.OSsysname,
            hostname=self.hostname,
            OSrelease=self.OSrelease,
            OSVersion=self.OSVersion,
            hostId=self.hostId,
        )


# Collector watches the world and decides what happened.
class Proccess_Collector_Decider:
    def __init__(self):
        self._seen_procs: set[int] = set()
        self.agent: agent_info = Agent().get_agent_info()
        self.previous_proc_list = {}

    def poll(self):
        events: list[EventModel] = []

        procs = {
            p.pid: processinfo(**p.info)
            for p in psutil.process_iter(
                [
                    "pid",
                    "ppid",
                    "name",
                    "exe",
                    "create_time",
                    "terminal",
                    "cmdline",
                    "uids",
                    "username",
                    "cwd",
                ]
            )
        }

        # First iteration ignore current running process
        if not self._seen_procs:
            self._seen_procs = set(procs.keys())
            self.previous_proc_list = procs.copy()
            return events

        # process start
        for pid, proc in procs.items():
            if pid not in self._seen_procs:
                events.append(
                    EventFactory.process_start(
                        proc=proc, agent=self.agent, network=None
                    )
                )
        # print("Debug:", procs.keys())
        for pid, proc in self.previous_proc_list.items():
            if pid not in procs.keys():
                events.append(
                    EventFactory.process_exit(proc=proc, agent=self.agent, network=None)
                )
        # process exit
        # for pid in list(self._seen_procs):
        #    if pid not in procs.keys():
        #        for pid2, proc in self.previous_proc_list.items():
        #            if pid == pid2:
        #                events.append(
        #                    EventFactory.process_exit(
        #                        proc=proc, agent=self.agent, network=None
        #                    )
        #                )

        self._seen_procs = set(procs.keys())
        return events


def count_open_connections():
    connections = psutil.net_connections()
    return len(connections)


def p_key(d):
    return (d.get("ppid"), d.get("pid"), d.get("proc_name"))


if __name__ == "__main__":
    from time import sleep

    pc = Proccess_Collector_Decider()

    while 1:
        events = pc.poll()

        print(len(events))
        print(events)

        sleep(3)
