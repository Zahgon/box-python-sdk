import io

import time
from collections import OrderedDict
from dataclasses import dataclass
from typing import Optional, Dict, Union, Tuple
from sys import version_info as py_version

import requests
from requests import RequestException, Session, Response
from requests_toolbelt import MultipartEncoder

from ..internal.logging import DataSanitizer
from .retries import BoxRetryStrategy
from ..networking.fetch_options import FetchOptions
from ..networking.fetch_response import FetchResponse
from ..box.errors import BoxAPIError, BoxSDKError, RequestInfo, ResponseInfo
from ..internal.utils import ByteStream, ResponseByteStream
from ..networking.network_client import NetworkClient
from ..networking.timeout_config import TimeoutConfig
from ..serialization.json import (
    sd_to_json,
    sd_to_url_params,
    json_to_serialized_data,
)
from ..networking.version import __version__

SDK_VERSION = __version__
USER_AGENT_HEADER = f'box-python-generated-sdk-{SDK_VERSION}'
X_BOX_UA_HEADER = (
    f'agent=box-python-generated-sdk/{SDK_VERSION}; '
    f'env=python/{py_version.major}.{py_version.minor}.{py_version.micro}'
)


@dataclass
class APIRequest:
    method: str
    url: str
    headers: Dict[str, str]
    params: Dict[str, str]
    data: Optional[Union[str, ByteStream, MultipartEncoder]]
    allow_redirects: bool = True
    timeout: Optional[Tuple[Optional[float], Optional[float]]] = None


@dataclass
class APIResponse:
    network_response: Optional[Response] = None
    reauthentication_needed: Optional[bool] = False
    raised_exception: Optional[Exception] = None

    def get_header(
        self, header_name: str, default_value: Optional[str] = None
    ) -> Optional[str]:
        pass


class BoxNetworkClient(NetworkClient):
    def __init__(self, requests_session: Optional[Session] = None):
        super().__init__()
        self.requests_session = requests_session or requests.Session()

    def fetch(self, options: 'FetchOptions') -> FetchResponse:
        pass

    def _prepare_request(
        self, options: 'FetchOptions', reauthenticate: bool = False
    ) -> APIRequest:
        pass

    @staticmethod
    def _get_request_timeout(
        options: 'FetchOptions',
    ) -> Optional[Tuple[Optional[float], Optional[float]]]:
        """
        Derive requests timeout tuple (connect, read) in seconds.

        Uses `options.network_session.timeout_config` when present.
        The timeout config values are expected to be in milliseconds.
        """
        pass

    @staticmethod
    def _prepare_headers(
        options: 'FetchOptions', reauthenticate: bool = False
    ) -> Dict[str, str]:
        pass

    @staticmethod
    def _prepare_body(
        content_type: str, data: Union[dict, ByteStream]
    ) -> Optional[Union[str, ByteStream]]:
        pass

    def _make_request(self, request: APIRequest) -> APIResponse:
        pass

    @staticmethod
    def _raise_on_unsuccessful_request(
        request: APIRequest, response: APIResponse, data_sanitizer: DataSanitizer
    ) -> None:
        pass

    @staticmethod
    def _get_multipart_stream_positions(options: 'FetchOptions') -> dict:
        pass

    @staticmethod
    def _get_options_stream_position(options: 'FetchOptions') -> int:
        pass

    @staticmethod
    def _validate_seekable(stream: ByteStream, raised_exception: Optional[Exception]):
        pass

    @staticmethod
    def _read_json_body(response_body: str) -> dict:
        pass

    def _reset_stream(
        self,
        stream: ByteStream,
        original_position: int,
        raised_exception: Optional[Exception],
    ):
        pass

    def _reset_options_stream(
        self,
        options: 'FetchOptions',
        filestream_position: int,
        raised_exception: Optional[Exception],
    ):
        pass

    def _reset_multipart_streams(
        self,
        options: 'FetchOptions',
        multipart_streams_positions: dict,
        raised_exception: Optional[Exception],
    ):
        pass
