from typing import Optional

from typing import Dict

from box_sdk_gen.serialization.json import serialize

from typing import List

from box_sdk_gen.schemas.post_o_auth_2_token import PostOAuth2TokenGrantTypeField

from box_sdk_gen.schemas.post_o_auth_2_token import PostOAuth2TokenSubjectTokenTypeField

from box_sdk_gen.networking.auth import Authentication

from box_sdk_gen.networking.network import NetworkSession

from box_sdk_gen.schemas.access_token import AccessToken

from box_sdk_gen.schemas.post_o_auth_2_token import PostOAuth2Token

from box_sdk_gen.schemas.post_o_auth_2_revoke import PostOAuth2Revoke

from box_sdk_gen.managers.authorization import AuthorizationManager

from box_sdk_gen.box.token_storage import TokenStorage

from box_sdk_gen.box.token_storage import InMemoryTokenStorage

from box_sdk_gen.serialization.json import sd_to_url_params

from box_sdk_gen.internal.utils import prepare_params

from box_sdk_gen.box.errors import BoxSDKError

from box_sdk_gen.serialization.json import SerializedData


class OAuthConfig:
    def __init__(
        self, client_id: str, client_secret: str, *, token_storage: TokenStorage = None
    ):
        if token_storage is None:
            token_storage = InMemoryTokenStorage()
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_storage = token_storage


class GetAuthorizeUrlOptions:
    def __init__(
        self,
        *,
        client_id: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        response_type: Optional[str] = None,
        state: Optional[str] = None,
        scope: Optional[str] = None
    ):
        """
        :param client_id: Box API key used for identifying the application the user is authenticating with, defaults to None
        :type client_id: Optional[str], optional
        :param redirect_uri: The URI to which Box redirects the browser after the user has granted or denied the application permission. This URI match one of the redirect URIs in the configuration of your application., defaults to None
        :type redirect_uri: Optional[str], optional
        :param response_type: The type of response we would like to receive., defaults to None
        :type response_type: Optional[str], optional
        :param state: A custom string of your choice. Box will pass the same string to the redirect URL when authentication is complete. This parameter can be used to identify a user on redirect, as well as protect against hijacked sessions and other exploits., defaults to None
        :type state: Optional[str], optional
        :param scope: A space-separated list of application scopes you'd like to authenticate the user for. This defaults to all the scopes configured for the application in its configuration page., defaults to None
        :type scope: Optional[str], optional
        """
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.response_type = response_type
        self.state = state
        self.scope = scope


class BoxOAuth(Authentication):
    def __init__(self, config: OAuthConfig, **kwargs):
        """
        :param config: Configuration object of OAuth.
        :type config: OAuthConfig
        """
        super().__init__(**kwargs)
        self.config = config
        self.token_storage = self.config.token_storage

    def get_authorize_url(self, *, options: GetAuthorizeUrlOptions = None) -> str:
        """
        Get the authorization URL for the app user.
        """
        pass

    def get_tokens_authorization_code_grant(
        self,
        authorization_code: str,
        *,
        network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        """
        Acquires token info using an authorization code.
        :param authorization_code: The authorization code to use to get tokens.
        :type authorization_code: str
        :param network_session: An object to keep network session state, defaults to None
        :type network_session: Optional[NetworkSession], optional
        """
        pass

    def retrieve_token(
        self, *, network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        """
        Get the current access token. If the current access token is expired or not found, this method will attempt to refresh the token.
        :param network_session: An object to keep network session state, defaults to None
        :type network_session: Optional[NetworkSession], optional
        """
        pass

    def refresh_token(
        self, *, network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        """
        Get a new access token for the platform app user.
        :param network_session: An object to keep network session state, defaults to None
        :type network_session: Optional[NetworkSession], optional
        """
        pass

    def retrieve_authorization_header(
        self, *, network_session: Optional[NetworkSession] = None
    ) -> str:
        pass

    def revoke_token(self, *, network_session: Optional[NetworkSession] = None) -> None:
        """
        Revoke an active Access Token, effectively logging a user out that has been previously authenticated.
        :param network_session: An object to keep network session state, defaults to None
        :type network_session: Optional[NetworkSession], optional
        """
        pass

    def downscope_token(
        self,
        scopes: List[str],
        *,
        resource: Optional[str] = None,
        shared_link: Optional[str] = None,
        network_session: Optional[NetworkSession] = None
    ) -> AccessToken:
        """
        Downscope access token to the provided scopes. Returning a new access token with the provided scopes, with the original access token unchanged.
        :param scopes: The scope(s) to apply to the resulting token.
        :type scopes: List[str]
        :param resource: The file or folder to get a downscoped token for. If None and shared_link None, the resulting token will not be scoped down to just a single item. The resource should be a full URL to an item, e.g. https://api.box.com/2.0/files/123456., defaults to None
        :type resource: Optional[str], optional
        :param shared_link: The shared link to get a downscoped token for. If None and item None, the resulting token will not be scoped down to just a single item., defaults to None
        :type shared_link: Optional[str], optional
        :param network_session: An object to keep network session state, defaults to None
        :type network_session: Optional[NetworkSession], optional
        """
        pass
