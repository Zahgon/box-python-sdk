from enum import Enum

from box_sdk_gen.internal.base_object import BaseObject

from typing import Optional

from typing import Dict

from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.serialization.json import deserialize

from box_sdk_gen.serialization.json import serialize

from box_sdk_gen.networking.fetch_options import ResponseFormat

from box_sdk_gen.schemas.terms_of_service_user_statuses import (
    TermsOfServiceUserStatuses,
)

from box_sdk_gen.schemas.client_error import ClientError

from box_sdk_gen.schemas.terms_of_service_user_status import TermsOfServiceUserStatus

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


class CreateTermsOfServiceStatusForUserTosTypeField(str, Enum):
    TERMS_OF_SERVICE = 'terms_of_service'


class CreateTermsOfServiceStatusForUserTos(BaseObject):
    _discriminator = 'type', {'terms_of_service'}

    def __init__(
        self,
        id: str,
        *,
        type: CreateTermsOfServiceStatusForUserTosTypeField = CreateTermsOfServiceStatusForUserTosTypeField.TERMS_OF_SERVICE,
        **kwargs
    ):
        """
        :param id: The ID of terms of service.
        :type id: str
        :param type: The type of object., defaults to CreateTermsOfServiceStatusForUserTosTypeField.TERMS_OF_SERVICE
        :type type: CreateTermsOfServiceStatusForUserTosTypeField, optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class CreateTermsOfServiceStatusForUserUserTypeField(str, Enum):
    USER = 'user'


class CreateTermsOfServiceStatusForUserUser(BaseObject):
    _discriminator = 'type', {'user'}

    def __init__(
        self,
        id: str,
        *,
        type: CreateTermsOfServiceStatusForUserUserTypeField = CreateTermsOfServiceStatusForUserUserTypeField.USER,
        **kwargs
    ):
        """
        :param id: The ID of user.
        :type id: str
        :param type: The type of object., defaults to CreateTermsOfServiceStatusForUserUserTypeField.USER
        :type type: CreateTermsOfServiceStatusForUserUserTypeField, optional
        """
        super().__init__(**kwargs)
        self.id = id
        self.type = type


class TermsOfServiceUserStatusesManager:
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

    def get_terms_of_service_user_statuses(
        self,
        tos_id: str,
        *,
        user_id: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> TermsOfServiceUserStatuses:
        """
        Retrieves an overview of users and their status for a

        terms of service, including Whether they have accepted


        the terms and when.

        :param tos_id: The ID of the terms of service.
        :type tos_id: str
        :param user_id: Limits results to the given user ID., defaults to None
        :type user_id: Optional[str], optional
        :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def create_terms_of_service_status_for_user(
        self,
        tos: CreateTermsOfServiceStatusForUserTos,
        user: CreateTermsOfServiceStatusForUserUser,
        is_accepted: bool,
        *,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> TermsOfServiceUserStatus:
        """
        Sets the status for a terms of service for a user.
        :param tos: The terms of service to set the status for.
        :type tos: CreateTermsOfServiceStatusForUserTos
        :param user: The user to set the status for.
        :type user: CreateTermsOfServiceStatusForUserUser
        :param is_accepted: Whether the user has accepted the terms.
        :type is_accepted: bool
        :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def update_terms_of_service_status_for_user_by_id(
        self,
        terms_of_service_user_status_id: str,
        is_accepted: bool,
        *,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> TermsOfServiceUserStatus:
        """
                Updates the status for a terms of service for a user.
                :param terms_of_service_user_status_id: The ID of the terms of service status.
        Example: "324234"
                :type terms_of_service_user_status_id: str
                :param is_accepted: Whether the user has accepted the terms.
                :type is_accepted: bool
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass
