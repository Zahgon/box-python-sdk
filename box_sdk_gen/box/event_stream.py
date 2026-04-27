import threading
from enum import Enum
from typing import Optional, Generator

from ..box.errors import BoxSDKError
from ..schemas.events import Events
from ..schemas.event import Event
from ..schemas.realtime_server import RealtimeServer
from ..networking.fetch_options import FetchOptions, ResponseFormat
from ..networking.fetch_response import FetchResponse


class RealtimeServerEvent(str, Enum):
    NEW_CHANGE = 'new_change'
    RECONNECT = 'reconnect'


class EventStreamAction(str, Enum):
    FETCH_EVENTS = 'fetch_events'
    RECONNECT = 'reconnect'
    RETRY = 'retry'
    STOP = 'stop'


class EventStream:
    """
    EventStream is an iterator that fetches events from the Box API.
    It uses long polling to receive real-time updates.
    This class is designed to be used as a Python iterator.

    Example usage:
        events_stream = client.events.get_event_stream()
        for event in events_stream:
            print(event)
    """

    def __init__(self, *, events_manager, query_params, headers_input):
        """
        Initialize the EventStream.

        :param events_manager: The EventsManager instance which provides relevant methods to fetch events.
        :param query_params: The query parameters to use for fetching events.
        :param headers_input: The headers to include in the request.
        """
        self._events_manager = events_manager
        self._query_params = query_params
        self._headers_input = headers_input
        self._stream_position = query_params.stream_position or 'now'
        self._long_polling_info: Optional[RealtimeServer] = None
        self._long_polling_retries: int = 0
        self._started: bool = False
        self._stopped: bool = False
        self._stop_event = threading.Event()
        self._deduplication_size = 1000
        self._dedupHash = dict()

    def __iter__(self) -> Generator[Event, None, None]:
        """Make EventStream iterable. Yields Event objects."""
        return self._event_generator()

    def _event_generator(self) -> Generator[Event, None, None]:
        """Generator that yields Event objects from the stream."""
        pass

    def stop(self):
        """Stop the event stream."""
        pass

    def _get_long_poll_info(self):
        """Fetch long polling info from the server."""
        pass

    def _get_long_poll_info_and_poll(self) -> str:
        """Get long polling info and perform a long poll, returning the action to take."""
        pass

    def _do_long_poll(self) -> str:
        """Perform the long polling request and return action to take."""
        pass

    def _fetch_events(self) -> Generator[Event, None, None]:
        """Fetch events from the API and yield Event objects."""
        pass
