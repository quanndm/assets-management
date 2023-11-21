from datetime import timedelta


class ConfigJWT():
    access_token_lifetime: timedelta
    refresh_token_lifetime: timedelta
    rotate_refresh_tokens: bool
    blacklist_after_rotation: bool

    signing_key: str
    verifying_key: str | None
    algorithm: str
    issuer: str | None
    audience: str | None

    auth_header_types: tuple[str]
    user_id_field: str
    user_id_claim: str

    auth_token_classes: tuple[str]
    token_type_claim: str

    jti_claim: str

    sliding_token_refresh_exp_claim: str
    sliding_token_lifetime: timedelta
    sliding_token_refresh_lifetime: timedelta

    def __init__(self, secret_key: str) -> None:
        self.access_token_lifetime = timedelta(minutes=30)
        self.refresh_token_lifetime = timedelta(days=1)
        self.rotate_refresh_tokens = False
        self.blacklist_after_rotation = True

        self.algorithm = 'HS256'
        self.signing_key = secret_key
        self.verifying_key = None
        self.audience = None
        self.issuer = None

        self.auth_header_types = ('Bearer',)
        self.user_id_field = 'id'
        self.user_id_claim = 'user_id'

        self.auth_token_classes = (
            'rest_framework_simplejwt.tokens.AccessToken',)
        self.token_type_claim = 'token_type'

        self.jti_claim = 'jti'

        self.sliding_token_refresh_exp_claim = 'refresh_exp'
        self.sliding_token_lifetime = timedelta(minutes=30)
        self.sliding_token_refresh_lifetime = timedelta(days=1)

    @classmethod
    def get_instance(cls, secret_key: str):
        if not hasattr(cls, '_instance'):
            cls._instance = cls(secret_key)
        return cls._instance

    def get_config(self) -> dict[str, str | timedelta | bool | tuple[str] | None]:
        return {
            'ACCESS_TOKEN_LIFETIME': self.access_token_lifetime,
            'REFRESH_TOKEN_LIFETIME': self.refresh_token_lifetime,
            'ROTATE_REFRESH_TOKENS': self.rotate_refresh_tokens,
            'BLACKLIST_AFTER_ROTATION': self.blacklist_after_rotation,

            'ALGORITHM': self.algorithm,
            'SIGNING_KEY': self.signing_key,
            'VERIFYING_KEY': self.verifying_key,
            'AUDIENCE': self.audience,
            'ISSUER': self.issuer,

            'AUTH_HEADER_TYPES': self.auth_header_types,
            'USER_ID_FIELD': self.user_id_field,
            'USER_ID_CLAIM': self.user_id_claim,

            'AUTH_TOKEN_CLASSES': self.auth_token_classes,
            'TOKEN_TYPE_CLAIM': self.token_type_claim,

            'JTI_CLAIM': self.jti_claim,

            'SLIDING_TOKEN_REFRESH_EXP_CLAIM': self.sliding_token_refresh_exp_claim,
            'SLIDING_TOKEN_LIFETIME': self.sliding_token_lifetime,
            'SLIDING_TOKEN_REFRESH_LIFETIME': self.sliding_token_refresh_lifetime,
        }
