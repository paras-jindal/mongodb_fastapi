from typing import List, Optional
from datetime import date, datetime
from pydantic import BaseModel,  Field
from datetime import datetime


class AudiobookSchema(BaseModel):
    title: str = Field(..., max_length=100)
    author: str = Field(..., max_length=100)
    narrator: str = Field(..., max_length=100)
    duration: int = Field(..., ge=0)
    uploadtime: datetime = Field(...)


class UpdateAudiobookModel(BaseModel):
    title: Optional[str]
    author: Optional[str]
    narrator: Optional[str]
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
