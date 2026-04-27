from enum import Enum

from box_sdk_gen.internal.base_object import BaseObject

from typing import Optional

from typing import Dict

from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.serialization.json import deserialize

from box_sdk_gen.serialization.json import serialize

from box_sdk_gen.networking.fetch_options import ResponseFormat

from box_sdk_gen.schemas.watermark import Watermark

from box_sdk_gen.schemas.client_error import ClientError

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


class UpdateFolderWatermarkWatermarkImprintField(str, Enum):
    DEFAULT = 'default'


class UpdateFolderWatermarkWatermark(BaseObject):
    def __init__(
        self,
        *,
        imprint: UpdateFolderWatermarkWatermarkImprintField = UpdateFolderWatermarkWatermarkImprintField.DEFAULT,
        **kwargs
    ):
        """
                :param imprint: The type of watermark to apply.

        Currently only supports one option., defaults to UpdateFolderWatermarkWatermarkImprintField.DEFAULT
                :type imprint: UpdateFolderWatermarkWatermarkImprintField, optional
        """
        super().__init__(**kwargs)
        self.imprint = imprint


class FolderWatermarksManager:
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

    def get_folder_watermark(
        self,
        folder_id: str,
        *,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> Watermark:
        """
                Retrieve the watermark for a folder.
                :param folder_id: The unique identifier that represent a folder.

        The ID for any folder can be determined
        by visiting this folder in the web application
        and copying the ID from the URL. For example,
        for the URL `https://*.app.box.com/folder/123`
        the `folder_id` is `123`.

        The root folder of a Box account is
        always represented by the ID `0`.
        Example: "12345"
                :type folder_id: str
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def update_folder_watermark(
        self,
        folder_id: str,
        watermark: UpdateFolderWatermarkWatermark,
        *,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> Watermark:
        """
                Applies or update a watermark on a folder.
                :param folder_id: The unique identifier that represent a folder.

        The ID for any folder can be determined
        by visiting this folder in the web application
        and copying the ID from the URL. For example,
        for the URL `https://*.app.box.com/folder/123`
        the `folder_id` is `123`.

        The root folder of a Box account is
        always represented by the ID `0`.
        Example: "12345"
                :type folder_id: str
                :param watermark: The watermark to imprint on the folder.
                :type watermark: UpdateFolderWatermarkWatermark
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def delete_folder_watermark(
        self,
        folder_id: str,
        *,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> None:
        """
                Removes the watermark from a folder.
                :param folder_id: The unique identifier that represent a folder.

        The ID for any folder can be determined
        by visiting this folder in the web application
        and copying the ID from the URL. For example,
        for the URL `https://*.app.box.com/folder/123`
        the `folder_id` is `123`.

        The root folder of a Box account is
        always represented by the ID `0`.
        Example: "12345"
                :type folder_id: str
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass
