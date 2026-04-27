import json
from typing import Dict, get_origin, Union, Type
from urllib.parse import urlencode

from ..internal.base_object import BaseObject

SerializedData = Dict


def json_to_serialized_data(data: str) -> SerializedData:
    pass


def sd_to_json(data: SerializedData) -> str:
    pass


def sd_to_url_params(data: SerializedData) -> str:
    pass


def get_sd_value_by_key(data: SerializedData, key: str):
    pass


def serialize(obj: Union[BaseObject, dict, list]) -> SerializedData:
    pass


def deserialize(value: SerializedData, type: Type[BaseObject]):
    pass


def sanitized_value() -> str:
    pass


def sanitize_serialized_data(
    sd: SerializedData, keys_to_sanitize: Dict[str, str]
) -> SerializedData:
    pass
