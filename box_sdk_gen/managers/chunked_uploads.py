from typing import List

from typing import Optional

from typing import Dict

from box_sdk_gen.serialization.json import serialize

from box_sdk_gen.serialization.json import deserialize

from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.networking.fetch_options import ResponseFormat

from box_sdk_gen.internal.utils import Buffer

from box_sdk_gen.internal.utils import HashName

from box_sdk_gen.internal.utils import Iterator

from box_sdk_gen.schemas.upload_session import UploadSession

from box_sdk_gen.schemas.client_error import ClientError

from box_sdk_gen.schemas.uploaded_part import UploadedPart

from box_sdk_gen.schemas.upload_parts import UploadParts

from box_sdk_gen.schemas.files import Files

from box_sdk_gen.schemas.upload_part import UploadPart

from box_sdk_gen.box.errors import BoxSDKError

from box_sdk_gen.networking.auth import Authentication

from box_sdk_gen.networking.network import NetworkSession

from box_sdk_gen.networking.fetch_options import FetchOptions

from box_sdk_gen.networking.fetch_response import FetchResponse

from box_sdk_gen.internal.utils import prepare_params

from box_sdk_gen.internal.utils import to_string

from box_sdk_gen.internal.utils import ByteStream

from box_sdk_gen.serialization.json import SerializedData

from box_sdk_gen.serialization.json import sd_to_json

from box_sdk_gen.internal.utils import generate_byte_stream_from_buffer

from box_sdk_gen.internal.utils import hex_to_base_64

from box_sdk_gen.internal.utils import iterate_chunks

from box_sdk_gen.internal.utils import read_byte_stream

from box_sdk_gen.internal.utils import reduce_iterator

from box_sdk_gen.internal.utils import Hash

from box_sdk_gen.internal.utils import buffer_length

from box_sdk_gen.schemas.file_full import FileFull


class _PartAccumulator:
    def __init__(
        self,
        last_index: int,
        parts: List[UploadPart],
        file_size: int,
        upload_part_url: str,
        file_hash: Hash,
    ):
        self.last_index = last_index
        self.parts = parts
        self.file_size = file_size
        self.upload_part_url = upload_part_url
        self.file_hash = file_hash


class ChunkedUploadsManager:
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

    def create_file_upload_session(
        self,
        folder_id: str,
        file_size: int,
        file_name: str,
        *,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> UploadSession:
        """
        Creates an upload session for a new file.
        :param folder_id: The ID of the folder to upload the new file to.
        :type folder_id: str
        :param file_size: The total number of bytes of the file to be uploaded.
        :type file_size: int
        :param file_name: The name of new file.
        :type file_name: str
        :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def create_file_upload_session_for_existing_file(
        self,
        file_id: str,
        file_size: int,
        *,
        file_name: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> UploadSession:
        """
                Creates an upload session for an existing file.
                :param file_id: The unique identifier that represents a file.

        The ID for any file can be determined
        by visiting a file in the web application
        and copying the ID from the URL. For example,
        for the URL `https://*.app.box.com/files/123`
        the `file_id` is `123`.
        Example: "12345"
                :type file_id: str
                :param file_size: The total number of bytes of the file to be uploaded.
                :type file_size: int
                :param file_name: The optional new name of new file., defaults to None
                :type file_name: Optional[str], optional
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def get_file_upload_session_by_url(
        self, url: str, *, extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> UploadSession:
        """
        Using this method with urls provided in response when creating a new upload session is preferred to use over GetFileUploadSessionById method.

        This allows to always upload your content to the closest Box data center and can significantly improve upload speed.


         Return information about an upload session.


        The actual endpoint URL is returned by the [`Create upload session`](https://developer.box.com/reference/post-files-upload-sessions) endpoint.

        :param url: URL of getFileUploadSessionById method
        :type url: str
        :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def get_file_upload_session_by_id(
        self,
        upload_session_id: str,
        *,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> UploadSession:
        """
                Return information about an upload session.

                The actual endpoint URL is returned by the [`Create upload session`](https://developer.box.com/reference/post-files-upload-sessions) endpoint.

                :param upload_session_id: The ID of the upload session.
        Example: "D5E3F7A"
                :type upload_session_id: str
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def upload_file_part_by_url(
        self,
        url: str,
        request_body: ByteStream,
        digest: str,
        content_range: str,
        *,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> UploadedPart:
        """
                Using this method with urls provided in response when creating a new upload session is preferred to use over UploadFilePart method.

                This allows to always upload your content to the closest Box data center and can significantly improve upload speed.


                 Uploads a chunk of a file for an upload session.


                The actual endpoint URL is returned by the [`Create upload session`](https://developer.box.com/reference/post-files-upload-sessions)


                and [`Get upload session`](https://developer.box.com/reference/get-files-upload-sessions-id) endpoints.

                :param url: URL of uploadFilePart method
                :type url: str
                :param request_body: Request body of uploadFilePart method
                :type request_body: ByteStream
                :param digest: The [RFC3230][1] message digest of the chunk uploaded.

        Only SHA1 is supported. The SHA1 digest must be base64
        encoded. The format of this header is as
        `sha=BASE64_ENCODED_DIGEST`.

        To get the value for the `SHA` digest, use the
        openSSL command to encode the file part:
        `openssl sha1 -binary <FILE_PART_NAME> | base64`.

        [1]: https://tools.ietf.org/html/rfc3230
                :type digest: str
                :param content_range: The byte range of the chunk.

        Must not overlap with the range of a part already
        uploaded this session. Each partâ€™s size must be
        exactly equal in size to the part size specified
        in the upload session that you created.
        One exception is the last part of the file, as this can be smaller.

        When providing the value for `content-range`, remember that:

        * The lower bound of each part's byte range
          must be a multiple of the part size.
        * The higher bound must be a multiple of the part size - 1.
                :type content_range: str
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def upload_file_part(
        self,
        upload_session_id: str,
        request_body: ByteStream,
        digest: str,
        content_range: str,
        *,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> UploadedPart:
        """
                Uploads a chunk of a file for an upload session.

                The actual endpoint URL is returned by the [`Create upload session`](https://developer.box.com/reference/post-files-upload-sessions)


                and [`Get upload session`](https://developer.box.com/reference/get-files-upload-sessions-id) endpoints.

                :param upload_session_id: The ID of the upload session.
        Example: "D5E3F7A"
                :type upload_session_id: str
                :param request_body: Request body of uploadFilePart method
                :type request_body: ByteStream
                :param digest: The [RFC3230][1] message digest of the chunk uploaded.

        Only SHA1 is supported. The SHA1 digest must be base64
        encoded. The format of this header is as
        `sha=BASE64_ENCODED_DIGEST`.

        To get the value for the `SHA` digest, use the
        openSSL command to encode the file part:
        `openssl sha1 -binary <FILE_PART_NAME> | base64`.

        [1]: https://tools.ietf.org/html/rfc3230
                :type digest: str
                :param content_range: The byte range of the chunk.

        Must not overlap with the range of a part already
        uploaded this session. Each partâ€™s size must be
        exactly equal in size to the part size specified
        in the upload session that you created.
        One exception is the last part of the file, as this can be smaller.

        When providing the value for `content-range`, remember that:

        * The lower bound of each part's byte range
          must be a multiple of the part size.
        * The higher bound must be a multiple of the part size - 1.
                :type content_range: str
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def delete_file_upload_session_by_url(
        self, url: str, *, extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> None:
        """
        Using this method with urls provided in response when creating a new upload session is preferred to use over DeleteFileUploadSessionById method.

        This allows to always upload your content to the closest Box data center and can significantly improve upload speed.


         Abort an upload session and discard all data uploaded.


        This cannot be reversed.


        The actual endpoint URL is returned by the [`Create upload session`](https://developer.box.com/reference/post-files-upload-sessions)


        and [`Get upload session`](https://developer.box.com/reference/get-files-upload-sessions-id) endpoints.

        :param url: URL of deleteFileUploadSessionById method
        :type url: str
        :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
        :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def delete_file_upload_session_by_id(
        self,
        upload_session_id: str,
        *,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> None:
        """
                Abort an upload session and discard all data uploaded.

                This cannot be reversed.


                The actual endpoint URL is returned by the [`Create upload session`](https://developer.box.com/reference/post-files-upload-sessions)


                and [`Get upload session`](https://developer.box.com/reference/get-files-upload-sessions-id) endpoints.

                :param upload_session_id: The ID of the upload session.
        Example: "D5E3F7A"
                :type upload_session_id: str
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def get_file_upload_session_parts_by_url(
        self,
        url: str,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> UploadParts:
        """
                Using this method with urls provided in response when creating a new upload session is preferred to use over GetFileUploadSessionParts method.

                This allows to always upload your content to the closest Box data center and can significantly improve upload speed.


                 Return a list of the chunks uploaded to the upload session so far.


                The actual endpoint URL is returned by the [`Create upload session`](https://developer.box.com/reference/post-files-upload-sessions)


                and [`Get upload session`](https://developer.box.com/reference/get-files-upload-sessions-id) endpoints.

                :param url: URL of getFileUploadSessionParts method
                :type url: str
                :param offset: The offset of the item at which to begin the response.

        Queries with offset parameter value
        exceeding 10000 will be rejected
        with a 400 response., defaults to None
                :type offset: Optional[int], optional
                :param limit: The maximum number of items to return per page., defaults to None
                :type limit: Optional[int], optional
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def get_file_upload_session_parts(
        self,
        upload_session_id: str,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> UploadParts:
        """
                Return a list of the chunks uploaded to the upload session so far.

                The actual endpoint URL is returned by the [`Create upload session`](https://developer.box.com/reference/post-files-upload-sessions)


                and [`Get upload session`](https://developer.box.com/reference/get-files-upload-sessions-id) endpoints.

                :param upload_session_id: The ID of the upload session.
        Example: "D5E3F7A"
                :type upload_session_id: str
                :param offset: The offset of the item at which to begin the response.

        Queries with offset parameter value
        exceeding 10000 will be rejected
        with a 400 response., defaults to None
                :type offset: Optional[int], optional
                :param limit: The maximum number of items to return per page., defaults to None
                :type limit: Optional[int], optional
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def create_file_upload_session_commit_by_url(
        self,
        url: str,
        parts: List[UploadPart],
        digest: str,
        *,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> Optional[Files]:
        """
                Using this method with urls provided in response when creating a new upload session is preferred to use over CreateFileUploadSessionCommit method.

                This allows to always upload your content to the closest Box data center and can significantly improve upload speed.


                 Close an upload session and create a file from the uploaded chunks.


                The actual endpoint URL is returned by the [`Create upload session`](https://developer.box.com/reference/post-files-upload-sessions)


                and [`Get upload session`](https://developer.box.com/reference/get-files-upload-sessions-id) endpoints.

                :param url: URL of createFileUploadSessionCommit method
                :type url: str
                :param parts: The list details for the uploaded parts.
                :type parts: List[UploadPart]
                :param digest: The [RFC3230][1] message digest of the whole file.

        Only SHA1 is supported. The SHA1 digest must be Base64
        encoded. The format of this header is as
        `sha=BASE64_ENCODED_DIGEST`.

        [1]: https://tools.ietf.org/html/rfc3230
                :type digest: str
                :param if_match: Ensures this item hasn't recently changed before
        making changes.

        Pass in the item's last observed `etag` value
        into this header and the endpoint will fail
        with a `412 Precondition Failed` if it
        has changed since., defaults to None
                :type if_match: Optional[str], optional
                :param if_none_match: Ensures an item is only returned if it has changed.

        Pass in the item's last observed `etag` value
        into this header and the endpoint will fail
        with a `304 Not Modified` if the item has not
        changed since., defaults to None
                :type if_none_match: Optional[str], optional
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def create_file_upload_session_commit(
        self,
        upload_session_id: str,
        parts: List[UploadPart],
        digest: str,
        *,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        extra_headers: Optional[Dict[str, Optional[str]]] = None
    ) -> Optional[Files]:
        """
                Close an upload session and create a file from the uploaded chunks.

                The actual endpoint URL is returned by the [`Create upload session`](https://developer.box.com/reference/post-files-upload-sessions)


                and [`Get upload session`](https://developer.box.com/reference/get-files-upload-sessions-id) endpoints.

                :param upload_session_id: The ID of the upload session.
        Example: "D5E3F7A"
                :type upload_session_id: str
                :param parts: The list details for the uploaded parts.
                :type parts: List[UploadPart]
                :param digest: The [RFC3230][1] message digest of the whole file.

        Only SHA1 is supported. The SHA1 digest must be Base64
        encoded. The format of this header is as
        `sha=BASE64_ENCODED_DIGEST`.

        [1]: https://tools.ietf.org/html/rfc3230
                :type digest: str
                :param if_match: Ensures this item hasn't recently changed before
        making changes.

        Pass in the item's last observed `etag` value
        into this header and the endpoint will fail
        with a `412 Precondition Failed` if it
        has changed since., defaults to None
                :type if_match: Optional[str], optional
                :param if_none_match: Ensures an item is only returned if it has changed.

        Pass in the item's last observed `etag` value
        into this header and the endpoint will fail
        with a `304 Not Modified` if the item has not
        changed since., defaults to None
                :type if_none_match: Optional[str], optional
                :param extra_headers: Extra headers that will be included in the HTTP request., defaults to None
                :type extra_headers: Optional[Dict[str, Optional[str]]], optional
        """
        pass

    def _reducer(self, acc: _PartAccumulator, chunk: ByteStream) -> _PartAccumulator:
        pass

    def upload_big_file(
        self, file: ByteStream, file_name: str, file_size: int, parent_folder_id: str
    ) -> FileFull:
        """
        Starts the process of chunk uploading a big file. Should return a File object representing uploaded file.
        :param file: The stream of the file to upload.
        :type file: ByteStream
        :param file_name: The name of the file, which will be used for storage in Box.
        :type file_name: str
        :param file_size: The total size of the file for the chunked upload in bytes.
        :type file_size: int
        :param parent_folder_id: The ID of the folder where the file should be uploaded.
        :type parent_folder_id: str
        """
        pass
