from typing import Optional

from typing import List

from typing import Dict

from box_sdk_gen.serialization.json import serialize

from box_sdk_gen.serialization.json import deserialize

from box_sdk_gen.networking.fetch_options import ResponseFormat

from box_sdk_gen.schemas.session_termination_message import SessionTerminationMessage

from box_sdk_gen.schemas.client_error import ClientError

from box_sdk_gen.box.errors import BoxSDKError

from box_sdk_gen.networking.auth import Authentication

from box_sdk_gen.networking.network import NetworkSession

from box_sdk_gen.networking.fetch_options import FetchOptions

from box_sdk_gen.networking.fetch_response import FetchResponse

from box_sdk_gen.internal.utils import prepare_params

from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.internal.utils import ByteStream

from box_sdk_gen.serialization.json import SerializedData


class SessionTerminationManager:
    def __init__(
        self,
        *,
        auth: Optional[Authentication] = None,
        network_session: NetworkSession = None
    ):
        if network_session is None:
            network_session = NetworkSession()
        self.auth = auth
        self.network_session = network_session

    def terminate_users_sessions(
        self,
        user_ids: List[str],
        user_logins: List[str],
        *,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> SessionTerminationMessage:
        """
        Validates the roles and permissions of the user,

        and creates asynchronous jobs


        to terminate the user's sessions.


        Returns the status for the POST request.

        :param user_ids: A list of user IDs.
        :type user_ids: List[str]
        :param user_logins: A list of user logins.
        :type user_logins: List[str]
        :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def terminate_groups_sessions(
        self,
        group_ids: List[str],
        *,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> SessionTerminationMessage:
        """
        Validates the roles and permissions of the group,

        and creates asynchronous jobs


        to terminate the group's sessions.


        Returns the status for the POST request.

        :param group_ids: A list of group IDs.
        :type group_ids: List[str]
        :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass
