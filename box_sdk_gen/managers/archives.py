from typing import Optional

from typing import Dict

from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.serialization.json import deserialize

from box_sdk_gen.serialization.json import serialize

from box_sdk_gen.networking.fetch_options import ResponseFormat

from box_sdk_gen.schemas.v2025_r0.archives_v2025_r0 import ArchivesV2025R0

from box_sdk_gen.schemas.v2025_r0.client_error_v2025_r0 import ClientErrorV2025R0

from box_sdk_gen.parameters.v2025_r0.box_version_header_v2025_r0 import (
    BoxVersionHeaderV2025R0,
)

from box_sdk_gen.schemas.v2025_r0.archive_v2025_r0 import ArchiveV2025R0

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


class ArchivesManager:
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

    def get_archives_v2025_r0(
        self,
        *,
        limit: Optional[int] = None,
        marker: Optional[str] = None,
        box_version: BoxVersionHeaderV2025R0 = BoxVersionHeaderV2025R0._2025_0,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> ArchivesV2025R0:
        """
                Retrieves archives for an enterprise.

                To learn more about the archive APIs, see the [Archive API Guide](https://developer.box.com/guides/archives).

                :param limit: The maximum number of items to return per page., defaults to None
                :type limit: Optional[int], optional
                :param marker: Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination., defaults to None
                :type marker: Optional[str], optional
                :param box_version: Version header., defaults to BoxVersionHeaderV2025R0._2025_0
                :type box_version: BoxVersionHeaderV2025R0, optional
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def create_archive_v2025_r0(
        self,
        name: str,
        *,
        description: Optional[str] = None,
        storage_policy_id: Optional[str] = None,
        box_version: BoxVersionHeaderV2025R0 = BoxVersionHeaderV2025R0._2025_0,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> ArchiveV2025R0:
        """
        Creates an archive.

        To learn more about the archive APIs, see the [Archive API Guide](https://developer.box.com/guides/archives).

        :param name: The name of the archive.
        :type name: str
        :param description: The description of the archive., defaults to None
        :type description: Optional[str], optional
        :param storage_policy_id: The ID of the storage policy that the archive is assigned to., defaults to None
        :type storage_policy_id: Optional[str], optional
        :param box_version: Version header., defaults to BoxVersionHeaderV2025R0._2025_0
        :type box_version: BoxVersionHeaderV2025R0, optional
        :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def delete_archive_by_id_v2025_r0(
        self,
        archive_id: str,
        *,
        box_version: BoxVersionHeaderV2025R0 = BoxVersionHeaderV2025R0._2025_0,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> None:
        """
                Permanently deletes an archive.

                To learn more about the archive APIs, see the [Archive API Guide](https://developer.box.com/guides/archives).


                <Danger>


                This endpoint is currently unavailable. Please contact support for assistance.


                </Danger>

                :param archive_id: The ID of the archive.
        Example: "982312"
                :type archive_id: str
                :param box_version: Version header., defaults to BoxVersionHeaderV2025R0._2025_0
                :type box_version: BoxVersionHeaderV2025R0, optional
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def update_archive_by_id_v2025_r0(
        self,
        archive_id: str,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        box_version: BoxVersionHeaderV2025R0 = BoxVersionHeaderV2025R0._2025_0,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> ArchiveV2025R0:
        """
                Updates an archive.

                To learn more about the archive APIs, see the [Archive API Guide](https://developer.box.com/guides/archives).

                :param archive_id: The ID of the archive.
        Example: "982312"
                :type archive_id: str
                :param name: The name of the archive., defaults to None
                :type name: Optional[str], optional
                :param description: The description of the archive., defaults to None
                :type description: Optional[str], optional
                :param box_version: Version header., defaults to BoxVersionHeaderV2025R0._2025_0
                :type box_version: BoxVersionHeaderV2025R0, optional
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass
