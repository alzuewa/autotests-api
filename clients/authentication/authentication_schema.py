from pydantic import BaseModel, Field

from tools.fakers import fake


class TokenSchema(BaseModel):
    """
    Auth token structure
    """
    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')


class LoginRequestSchema(BaseModel):
    """
    Request structure for authentication.
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class LoginResponseSchema(BaseModel):
    """
    Auth response structure
    """
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    """
    Request structure for accessToken renew.
    """
    refresh_token: str = Field(alias='refreshToken', default_factory=fake.sentence)
