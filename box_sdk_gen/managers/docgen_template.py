from typing import Optional

from typing import Dict

from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.serialization.json import serialize

from box_sdk_gen.serialization.json import deserialize

from box_sdk_gen.schemas.v2025_r0.file_reference_v2025_r0 import FileReferenceV2025R0

from box_sdk_gen.networking.fetch_options import ResponseFormat

from box_sdk_gen.schemas.v2025_r0.doc_gen_template_base_v2025_r0 import (
    DocGenTemplateBaseV2025R0,
)

from box_sdk_gen.schemas.v2025_r0.client_error_v2025_r0 import ClientErrorV2025R0

from box_sdk_gen.parameters.v2025_r0.box_version_header_v2025_r0 import (
    BoxVersionHeaderV2025R0,
)

from box_sdk_gen.schemas.v2025_r0.doc_gen_template_create_request_v2025_r0 import (
    DocGenTemplateCreateRequestV2025R0,
)

from box_sdk_gen.schemas.v2025_r0.doc_gen_templates_v2025_r0 import (
    DocGenTemplatesV2025R0,
)

from box_sdk_gen.schemas.v2025_r0.doc_gen_template_v2025_r0 import DocGenTemplateV2025R0

from box_sdk_gen.schemas.v2025_r0.doc_gen_tags_v2025_r0 import DocGenTagsV2025R0

from box_sdk_gen.schemas.v2025_r0.doc_gen_tags_processing_message_v2025_r0 import (
    DocGenTagsProcessingMessageV2025R0,
)

from box_sdk_gen.schemas.v2025_r0.doc_gen_jobs_v2025_r0 import DocGenJobsV2025R0

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


class DocgenTemplateManager:
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

    def create_docgen_template_v2025_r0(
        self,
        file: FileReferenceV2025R0,
        *,
        box_version: BoxVersionHeaderV2025R0 = BoxVersionHeaderV2025R0._2025_0,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> DocGenTemplateBaseV2025R0:
        """
        Marks a file as a Box Doc Gen template.
        :param box_version: Version header., defaults to BoxVersionHeaderV2025R0._2025_0
        :type box_version: BoxVersionHeaderV2025R0, optional
        :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def get_docgen_templates_v2025_r0(
        self,
        *,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        box_version: BoxVersionHeaderV2025R0 = BoxVersionHeaderV2025R0._2025_0,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> DocGenTemplatesV2025R0:
        """
                Lists Box Doc Gen templates on which the user is a collaborator.
                :param marker: Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`., defaults to None
                :type marker: Optional[str], optional
                :param limit: The maximum number of items to return per page., defaults to None
                :type limit: Optional[int], optional
                :param box_version: Version header., defaults to BoxVersionHeaderV2025R0._2025_0
                :type box_version: BoxVersionHeaderV2025R0, optional
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def delete_docgen_template_by_id_v2025_r0(
        self,
        template_id: str,
        *,
        box_version: BoxVersionHeaderV2025R0 = BoxVersionHeaderV2025R0._2025_0,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> None:
        """
                Unmarks file as Box Doc Gen template.
                :param template_id: ID of the file which will no longer be marked as a Box Doc Gen template.
        Example: "123"
                :type template_id: str
                :param box_version: Version header., defaults to BoxVersionHeaderV2025R0._2025_0
                :type box_version: BoxVersionHeaderV2025R0, optional
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def get_docgen_template_by_id_v2025_r0(
        self,
        template_id: str,
        *,
        box_version: BoxVersionHeaderV2025R0 = BoxVersionHeaderV2025R0._2025_0,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> DocGenTemplateV2025R0:
        """
                Lists details of a specific Box Doc Gen template.
                :param template_id: The ID of a Box Doc Gen template.
        Example: 123
                :type template_id: str
                :param box_version: Version header., defaults to BoxVersionHeaderV2025R0._2025_0
                :type box_version: BoxVersionHeaderV2025R0, optional
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def get_docgen_template_tags_v2025_r0(
        self,
        template_id: str,
        *,
        template_version_id: Optional[str] = None,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        box_version: BoxVersionHeaderV2025R0 = BoxVersionHeaderV2025R0._2025_0,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> DocGenTagsV2025R0:
        """
                Lists all tags in a Box Doc Gen template.
                :param template_id: ID of template.
        Example: 123
                :type template_id: str
                :param template_version_id: Id of template version., defaults to None
                :type template_version_id: Optional[str], optional
                :param marker: Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`., defaults to None
                :type marker: Optional[str], optional
                :param limit: The maximum number of items to return per page., defaults to None
                :type limit: Optional[int], optional
                :param box_version: Version header., defaults to BoxVersionHeaderV2025R0._2025_0
                :type box_version: BoxVersionHeaderV2025R0, optional
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def get_docgen_template_job_by_id_v2025_r0(
        self,
        template_id: str,
        *,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
        box_version: BoxVersionHeaderV2025R0 = BoxVersionHeaderV2025R0._2025_0,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> DocGenJobsV2025R0:
        """
                Lists the users jobs which use this template.
                :param template_id: Id of template to fetch jobs for.
        Example: 123
                :type template_id: str
                :param marker: Defines the position marker at which to begin returning results. This is
        used when paginating using marker-based pagination.

        This requires `usemarker` to be set to `true`., defaults to None
                :type marker: Optional[str], optional
                :param limit: The maximum number of items to return per page., defaults to None
                :type limit: Optional[int], optional
                :param box_version: Version header., defaults to BoxVersionHeaderV2025R0._2025_0
                :type box_version: BoxVersionHeaderV2025R0, optional
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass
