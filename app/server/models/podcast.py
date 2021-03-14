from typing import List, Optional
from datetime import date, datetime
from pydantic import BaseModel,  Field


class PodcastSchema(BaseModel):
    name: str = Field(..., max_length=100)
    duration: int = Field(..., ge=0)
    uploadtime: datetime
    host: str = Field(..., max_length=100)
    participants: Optional[List[str]
                           ] = Field(..., max_length=100, max_items=10)


class UpdatePodcastModel(BaseModel):
    name: Optional[str]
    duration: Optional[int]
    uploadtime: Optional[datetime]
    host: Optional[str]
    Participants: Optional[List[str]]


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
