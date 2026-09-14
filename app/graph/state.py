from typing import  TypedDict

class SousState(TypedDict):
    messages: list
    image: str | None
    is_valid_photo: bool | None