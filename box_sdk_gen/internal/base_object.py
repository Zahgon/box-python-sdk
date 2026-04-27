from datetime import datetime, date
from enum import EnumMeta, Enum
from typing import get_args, get_origin, Union, Optional
from .null_value import NullValue


class BaseObject:
    _discriminator = (None, {})
    _json_to_fields_mapping = {}
    _fields_to_json_mapping = {}

    def __init__(self, **kwargs):
        self._raw_data: dict = {}
        self.__dict__.update(kwargs)

    @classmethod
    def from_dict(cls, data: dict):
        pass

    @property
    def raw_data(self):
        """
        Returns the raw json representation returned by the API
        :return: dict with the raw json data
        """
        pass

    def to_dict(self) -> dict:
        pass

    @classmethod
    def _deserialize(cls, key, value, annotation=None):
        pass

    @classmethod
    def _deserialize_list(cls, key, value, annotation: list):
        pass

    @classmethod
    def _deserialize_union(cls, key, value, annotation):
        pass

    @classmethod
    def _deserialize_enum(cls, key, value, annotation):
        pass

    @classmethod
    def _deserialize_datetime(cls, key, value, annotation):
        pass

    @classmethod
    def _deserialize_date(cls, key, value, annotation):
        pass

    @classmethod
    def _deserialize_nested_type(cls, key, value, annotation):
        pass

    def __repr__(self) -> str:
        return f'{self.__class__} {self.to_dict()}'
