from enum import Enum

from typing import Optional

from typing import Dict

from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.serialization.json import deserialize

from box_sdk_gen.serialization.json import serialize

from box_sdk_gen.networking.fetch_options import ResponseFormat

from box_sdk_gen.schemas.shield_information_barrier import ShieldInformationBarrier

from box_sdk_gen.schemas.client_error import ClientError

from box_sdk_gen.schemas.shield_information_barriers import ShieldInformationBarriers

from box_sdk_gen.schemas.enterprise_base import EnterpriseBase

from box_sdk_gen.box.errors import BoxSDKError

from box_sdk_gen.networking.auth import Authentication

from box_sdk_gen.networking.network import NetworkSession

from box_sdk_gen.networking.fetch_options import FetchOptions

from box_sdk_gen.networking.fetch_response import FetchResponse

from box_sdk_gen.internal.utils import prepare_params

from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.internal.utils import ByteStream

from box_sdk_gen.serialization.json import sd_to_json

from box_sdk_gen.serialization.json import SerializedData


class UpdateShieldInformationBarrierStatusStatus(str, Enum):
    PENDING = 'pending'
    DISABLED = 'disabled'


class ShieldInformationBarriersManager:
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

    def get_shield_information_barrier_by_id(
        self,
        shield_information_barrier_id: str,
        *,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> ShieldInformationBarrier:
        """
                Get shield information barrier based on provided ID.
                :param shield_information_barrier_id: The ID of the shield information barrier.
        Example: "1910967"
                :type shield_information_barrier_id: str
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def update_shield_information_barrier_status(
        self,
        id: str,
        status: UpdateShieldInformationBarrierStatusStatus,
        *,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> ShieldInformationBarrier:
        """
        Change status of shield information barrier with the specified ID.
        :param id: The ID of the shield information barrier.
        :type id: str
        :param status: The desired status for the shield information barrier.
        :type status: UpdateShieldInformationBarrierStatusStatus
        :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def get_shield_information_barriers(
        self,
        *,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> ShieldInformationBarriers:
        """
                Retrieves a list of shield information barrier objects

                for the enterprise of JWT.

                :param marker: Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination., defaults to None
                :type marker: Optional[str], optional
                :param limit: The maximum number of items to return per page., defaults to None
                :type limit: Optional[int], optional
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def create_shield_information_barrier(
        self,
        enterprise: EnterpriseBase,
        *,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> ShieldInformationBarrier:
        """
        Creates a shield information barrier to

        separate individuals/groups within the same


        firm and prevents confidential information passing between them.

        :param enterprise: The `type` and `id` of enterprise this barrier is under.
        :type enterprise: EnterpriseBase
        :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass
