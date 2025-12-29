from datetime import datetime
from .schemas import EventModel, EventType, agent_info, networkinfo, processinfo
from uuid import UUID, uuid4


def utc_now() -> datetime:
    return datetime.now()


def s_uuid() -> str:
    u_object: UUID = uuid4()
    return str(u_object)


class EventFactory:
    @staticmethod
    def process_start(
        proc: processinfo, agent: agent_info, network: networkinfo | None
    ) -> EventModel:
        return EventModel(
            event_id=s_uuid(),
            event_type=EventType.PROCESS_START,
            timestamp=utc_now(),
            process=proc,
            network=network,
            agent_info=agent,
        )

    @staticmethod
    def process_exit(
        proc: processinfo, agent: agent_info, network: networkinfo | None
    ) -> EventModel:
        return EventModel(
            event_id=s_uuid(),
            event_type=EventType.PROCESS_EXIT,
            timestamp=utc_now(),
            process=proc,
            network=network,
            agent_info=agent,
        )

    @staticmethod
    def new_network_connection(network: networkinfo, agent: agent_info) -> EventModel:
        return EventModel(
            event_id=s_uuid(),
            event_type=EventType.NET_CONN,
            timestamp=utc_now(),
            process=None,
            network=network,
            agent_info=agent,
        )

    @staticmethod
    def new_dns_query(agent: agent_info) -> EventModel:
        return EventModel(
            event_id=s_uuid(),
            event_type=EventType.DNS_QUERY,
            timestamp=utc_now(),
            process=None,  # Tbd later if needed
            network=None,  # Tbd later if needed
            agent_info=agent,
        )

    @staticmethod
    def heartbeat():
        pass
