import shelve
from abc import abstractmethod
from typing import Optional

from ..schemas.access_token import AccessToken


class TokenStorage:
    @abstractmethod
    def store(self, token: AccessToken) -> None:
        pass

    @abstractmethod
    def get(self) -> Optional[AccessToken]:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass


class InMemoryTokenStorage(TokenStorage):
    def __init__(self, token: Optional[AccessToken] = None):
        self._token = token

    def store(self, token: AccessToken) -> None:
        pass

    def get(self) -> Optional[AccessToken]:
        pass

    def clear(self) -> None:
        pass


class FileTokenStorage(TokenStorage):
    def __init__(self, filename: str = 'token_storage'):
        self.filename = filename

    def store(self, token: AccessToken) -> None:
        pass

    def get(self) -> Optional[AccessToken]:
        pass

    def clear(self) -> None:
        pass


class FileWithInMemoryCacheTokenStorage(TokenStorage):
    def __init__(self, filename: str = 'token_storage'):
        self.filename = filename
        self.cached_token: Optional[AccessToken] = None

    def store(self, token: AccessToken) -> None:
        pass

    def get(self) -> Optional[AccessToken]:
        pass

    def clear(self) -> None:
        pass
