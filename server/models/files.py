from typing import Optional
from datetime import datetime, time, timedelta
from pydantic import BaseModel, Field


class Song(BaseModel):
    ID: int = Field(...)
    name: str = Field(...,max_length=100)
    duration: int = Field(...,gt=0)
    upload_date: datetime = Field(..., gt=datetime.now())

    class Config:
        schema_extra = {
            "example": {
                "ID": "123456789",
                "name": "jai javan",
                "duration": 120,
                "upload_date": "10-10-2022"
            }
        }


class Podcast(BaseModel):
    ID: int = Field(...)
    name: str = Field(...,max_length=100)
    duration: int = Field(...,gt=0)
    upload_date: datetime = Field(..., gt=datetime.now())
    host:str =Field(...,max_length=100)
    participants : Optional[List[str]]=Field(max_length=10)

    class Config:
        schema_extra = {
            "example": {
                "ID": "123456789",
                "name": "jai javan",
                "duration": 120,
                "upload_date": "10-10-2022",
                "host":"Paras jindal",
                "participants":["acd","asdwq","xzca"]
            }
        }

class Audiobook(BaseModel):
    ID: int = Field(...)
    title: str = Field(...,max_length=100)
    author:str=Field(...,max_length=100)
    narrator:str=Field(...,max_length=100)
    duration: int = Field(...,gt=0)
    upload_date: datetime = Field(..., gt=datetime.now())

    class Config:
        schema_extra = {
            "example": {
                "ID": "123456789",
                "title": "jai javan",
                "author": "paras jindal",
                "narrator": "paras jindal",
                "duration": 120,
                "upload_date": "10-10-2022"
            }
        }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}