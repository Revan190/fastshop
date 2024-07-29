from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    """
    Model for representing an access token.
    """
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """
    A model for representing the data associated with a token.
    """
    email: EmailStr | None = None
