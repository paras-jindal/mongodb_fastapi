from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel,  Field
from .song import (
    SongSchema,
)
from .podcast import (
    PodcastSchema,
)
from .audiobook import (
    AudiobookSchema,
)


class AudioSchema(BaseModel):
    type: str = Field(...)
    songmetadata: Optional[SongSchema] = None
    podcastmetadata: Optional[PodcastSchema] = None
    audiobookmetadata: Optional[AudiobookSchema] = None


class UpdateAudioModel(BaseModel):
    type: Optional[str]
    songmetadata: Optional[SongSchema]
    podcastmetadata: Optional[PodcastSchema]
    audiobookmetadata: Optional[AudiobookSchema]


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
