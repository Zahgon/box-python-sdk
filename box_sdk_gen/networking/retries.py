from abc import abstractmethod

from typing import Optional

from box_sdk_gen.networking.fetch_options import FetchOptions

from box_sdk_gen.networking.fetch_response import FetchResponse

from box_sdk_gen.internal.utils import random


class RetryStrategy:
    def __init__(self):
        pass

    @abstractmethod
    def should_retry(
        self,
        fetch_options: FetchOptions,
        fetch_response: FetchResponse,
        attempt_number: int,
    ) -> bool:
        pass

    @abstractmethod
    def retry_after(
        self,
        fetch_options: FetchOptions,
        fetch_response: FetchResponse,
        attempt_number: int,
    ) -> float:
        pass


class BoxRetryStrategy(RetryStrategy):
    def __init__(
        self,
        *,
        max_attempts: int = 5,
        retry_randomization_factor: float = 0.5,
        retry_base_interval: float = 1,
        max_retries_on_exception: int = 2,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.max_attempts = max_attempts
        self.retry_randomization_factor = retry_randomization_factor
        self.retry_base_interval = retry_base_interval
        self.max_retries_on_exception = max_retries_on_exception

    def should_retry(
        self,
        fetch_options: FetchOptions,
        fetch_response: FetchResponse,
        attempt_number: int,
    ) -> bool:
        pass

    def retry_after(
        self,
        fetch_options: FetchOptions,
        fetch_response: FetchResponse,
        attempt_number: int,
    ) -> float:
        pass
