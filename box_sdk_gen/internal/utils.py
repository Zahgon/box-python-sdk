import base64
import datetime
import hashlib
import os
import re
import shutil
import uuid
import time
import hmac
from random import uniform
from enum import Enum
from io import SEEK_CUR, SEEK_END, SEEK_SET, BufferedIOBase, BytesIO
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar, BinaryIO

from abc import abstractmethod
from typing import Any

try:
    import jwt
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import serialization
except ImportError:
    jwt, default_backend, serialization = None, None, None

from .base_object import BaseObject
from ..serialization.json import sd_to_json, sanitized_value
from ..serialization.json import serialize
from .null_value import null

ByteStream = BufferedIOBase
OutputStream = BinaryIO
Buffer = bytes


class ResponseByteStream(ByteStream):
    def __init__(self, request_iterator):
        self._iterator = request_iterator
        self._buffer = b''
        self._position = 0
        self._eos = False

    def _read_from_iterator(self, size):
        """
        Read up to `size` bytes from the iterator into the buffer
        :param size: Number of bytes to read. If None, read the entire stream.
        """
        pass

    def tell(self):
        """
        Returns the current position in the stream
        :return:
        """
        pass

    def read(self, size=None):
        """
        Reads up to `size` bytes from the stream
        :param size: Read up to `size` bytes from the stream. If None read the entire stream.
        :return: Bytes read from the stream
        """
        pass

    def seek(self, position, whence=SEEK_SET):
        """
        Move the stream to given position
        :param position: Position to move to
        :param whence: One of SEEK_SET = 0, SEEK_CUR = 1 or SEEK_END = 2
        :return: The new position in the stream
        """
        pass


def get_env_var(name: str) -> str:
    pass


def get_uuid() -> str:
    pass


def decode_base_64(value: str) -> str:
    pass


def generate_byte_buffer(size: int) -> Buffer:
    pass


def generate_byte_stream_from_buffer(buffer: Buffer) -> ByteStream:
    pass


def generate_byte_stream(size: int) -> ByteStream:
    pass


def buffer_equals(buffer1: Buffer, buffer2: Buffer) -> bool:
    pass


def buffer_length(buffer: Buffer) -> int:
    pass


def decode_base_64_byte_stream(value: str) -> ByteStream:
    pass


def string_to_byte_stream(value: str) -> ByteStream:
    pass


def read_byte_stream(byte_stream: ByteStream) -> Buffer:
    pass


def write_input_stream_to_output_stream(
    input_stream: ByteStream, output_stream: OutputStream
):
    pass


def get_file_output_stream(file_path: str) -> OutputStream:
    pass


def close_file_output_stream(file_output_stream: OutputStream):
    pass


def read_buffer_from_file(path: str) -> bytes:
    pass


def prepare_params(map: Dict[str, Optional[str]]) -> Dict[str, str]:
    pass


def to_string(value: Any) -> Optional[str]:
    pass


class HashName(str, Enum):
    SHA1 = 'sha1'


class Hash:
    def __init__(self, algorithm: HashName):
        self.algorithm = algorithm
        self.hash = hashlib.sha1()

    def update_hash(self, data: Buffer):
        pass

    def digest_hash(self, encoding):
        pass


def hex_to_base_64(data: hex):
    pass


T = TypeVar('T')
Iterator = Iterable[T]
Accumulator = TypeVar('Accumulator')


def iterate_chunks(
    stream: ByteStream, chunk_size: int, file_size: int
) -> Iterable[ByteStream]:
    pass


def reduce_iterator(
    iterator: Iterator,
    reducer: Callable[[Accumulator, T], Accumulator],
    initial_value: Accumulator,
) -> Accumulator:
    pass


def read_text_from_file(file_path: str) -> str:
    pass


def is_browser() -> bool:
    pass


def get_epoch_time_in_seconds() -> int:
    pass


def get_value_from_object_raw_data(obj: BaseObject, key: str) -> Any:
    pass


class PrivateKeyDecryptor:
    """Class used for private key decryption in JWT auth."""

    @abstractmethod
    def decrypt_private_key(self, encryptedPrivateKey: str, passphrase: str) -> Any:
        """Decrypts private key using a passphrase."""
        pass


class DefaultPrivateKeyDecryptor(PrivateKeyDecryptor):
    def decrypt_private_key(self, encryptedPrivateKey: str, passphrase: str) -> Any:
        pass


class JwtAlgorithm(str, Enum):
    HS256 = 'HS256'
    HS384 = 'HS384'
    HS512 = 'HS512'
    RS256 = 'RS256'
    RS384 = 'RS384'
    RS512 = 'RS512'
    ES256 = 'ES256'
    ES384 = 'ES384'
    ES512 = 'ES512'
    PS256 = 'PS256'
    PS384 = 'PS384'
    PS512 = 'PS512'
    none = 'none'


class JwtSignOptions(BaseObject):
    def __init__(
        self,
        algorithm: JwtAlgorithm,
        headers: Dict[str, str] = None,
        audience: Optional[str] = None,
        issuer: Optional[str] = None,
        subject: Optional[str] = None,
        jwtid: Optional[str] = None,
        keyid: Optional[str] = None,
        private_key_decryptor: Optional[PrivateKeyDecryptor] = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        if headers is None:
            headers = {}
        self.algorithm = algorithm
        self.headers = headers
        self.audience = audience
        self.issuer = issuer
        self.subject = subject
        self.jwtid = jwtid
        self.keyid = keyid
        self.private_key_decryptor = (
            private_key_decryptor
            if private_key_decryptor is not None
            else DefaultPrivateKeyDecryptor()
        )


class JwtKey(BaseObject):
    def __init__(self, key: str, passphrase: str, **kwargs):
        super().__init__(**kwargs)
        self.key = key
        self.passphrase = passphrase


def encode_str_ascii_or_raise(passphrase: str) -> bytes:
    pass


def create_jwt_assertion(claims: dict, key: JwtKey, options: JwtSignOptions) -> str:
    pass


Date = datetime.date
DateTime = datetime.datetime


def date_to_string(date: Date) -> str:
    pass


def date_from_string(date: str) -> Date:
    pass


def date_time_to_string(date_time: DateTime) -> str:
    pass


def date_time_from_string(date_time: str) -> DateTime:
    pass


def date_time_to_epoch_seconds(date_time: DateTime) -> int:
    pass


def epoch_seconds_to_date_time(epoch_seconds: int) -> DateTime:
    pass


def delay_in_seconds(seconds: int):
    pass


def create_null():
    pass


def escape_unicode(value: str) -> str:
    pass


def compute_webhook_signature(
    body: str,
    headers: Dict[str, str],
    signature_key: str,
    escape_body: Optional[bool] = False,
) -> Optional[str]:
    """
    Computes the Hmac for the webhook notification given one signature key.

    :param body:
        The encoded webhook body.
    :param headers:
        The headers for the `Webhook` notification.
    :param signature_key:
        The `Webhook` signature key for this application.
    :param escape_body:
        Indicates if payload should be escaped or left as is.
    :return:
        An Hmac signature.
    """
    pass


def compare_signatures(
    expected_signature: Optional[str], received_signature: Optional[str]
) -> bool:
    pass


def random(min: float, max: float) -> float:
    pass


def sanitize_map(
    dictionary: Dict[str, str], keys_to_sanitize: Dict[str, str]
) -> Dict[str, str]:
    pass
