# shortener_app/schemas.py

from pydantic import BaseModel, validator


class URLBase(BaseModel):
    target_url: str
    custom_key: str = ""


class URL(URLBase):
    is_active: bool
    clicks: int

    class Config:
        orm_mode = True


class URLInfo(URL):
    """
    You could also add the two strings url and admin_url to URL.
    But by adding url and admin_url to the URLInfo subclass,
    you can use the data in your API without storing it in your database.
    """
    url: str
    admin_url: str
