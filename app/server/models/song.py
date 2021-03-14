from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel,  Field


class SongSchema(BaseModel):
    name: str = Field(..., max_length=100)
    duration: int = Field(..., ge=0)
    uploadtime: datetime = Field(...)


class UpdateSongModel(BaseModel):
    name: Optional[str]
    duration: Optional[int]
    uploadtime: Optional[datetime]


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
