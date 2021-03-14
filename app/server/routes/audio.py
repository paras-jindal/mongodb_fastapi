from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.params import Body

from ..database import (
    add_song,
    add_podcast,
    add_audiobook,
    retrieve_songs,
    retrieve_audiobooks,
    retrieve_podcasts,
    retrieve_song,
    retrieve_audiobook,
    retrieve_podcast,
    delete_song,
    delete_audiobook,
    delete_podcast,
    update_audiobook,
    update_podcast,
    update_song
)

from ..models.audio import (
    ErrorResponseModel,
    ResponseModel,
    AudioSchema,
    UpdateAudioModel,
)
router = APIRouter()


@router.post("/addaudio", response_description="Song data added into the database")
async def add_song_data(audio: AudioSchema):
    audio = jsonable_encoder(audio)
    if audio['type'].lower() == 'song':
        new_song = await add_song(audio)
        return ResponseModel(new_song, "Audio added successfully.")
    elif audio['type'].lower() == 'podcast':
        new_podcast = await add_podcast(audio)
        return ResponseModel(new_podcast, "Audio added successfully.")
    elif audio['type'].lower() == 'audiobook':
        new_audiobook = await add_audiobook(audio)
        return ResponseModel(new_audiobook, "Audio added successfully.")

    return ErrorResponseModel("An error occurred.", 400, "fill audiotype from following : song,podcast or audiobook")


@router.get("/{audioType}", response_description="audio retrieved")
async def get_audio(audioType: str):
    if audioType.lower() == 'song':
        audios = await retrieve_songs()
        if audios:
            return ResponseModel(audios, "audio data retrieved successfully")

    elif audioType.lower() == 'podcast':
        audios = await retrieve_podcasts()
        if audios:
            return ResponseModel(audios, "audio data retrieved successfully")
    elif audioType.lower() == 'audiobook':
        audios = await retrieve_audiobooks()
        if audios:
            return ResponseModel(audios, "audio data retrieved successfully")

    return ResponseModel(audios, "Empty list returned")


@router.get("/{audioType}/{id}", response_description="audio retrieved")
async def get_audiobyid(audioType: str, id: str):
    if audioType.lower() == 'song':
        audio = await retrieve_song(id)
        if audio:
            return ResponseModel(audio, "audio data retrieved successfully")
    elif audioType.lower() == 'podcast':
        audio = await retrieve_podcast(id)
        if audio:
            return ResponseModel(audio, "audio data retrieved successfully")
    elif audioType.lower() == 'audiobook':
        audio = await retrieve_audiobook(id)
        if audio:
            return ResponseModel(audio, "audio data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 400, "audio you are looking for doesn't exist.")


@router.delete("/{audioType}/{id}", response_description="audio retrieved")
async def delete_audiobyid(audioType: str, id: str):
    if audioType.lower() == 'song':
        deleted_audio = await delete_song(id)
        if deleted_audio:
            return ResponseModel(
                "Audio with ID: {} removed".format(
                    id), "Audio deleted successfully"
            )
    elif audioType.lower() == 'podcast':
        deleted_audio = await delete_podcast(id)
        if deleted_audio:
            return ResponseModel(
                "Audio with ID: {} removed".format(
                    id), "Audio deleted successfully"
            )
    elif audioType.lower() == 'audiobook':
        deleted_audio = await delete_audiobook(id)
        if deleted_audio:
            return ResponseModel(
                "Audio with ID: {} removed".format(
                    id), "Audio deleted successfully"
            )
    return ErrorResponseModel(
        "An error occurred", 400, "Audio with id {0} doesn't exist".format(id)
    )


@router.put("/{audioType}/{id}")
async def update_audio_data(audioType: str, id: str, req: UpdateAudioModel = Body(...)):

    if audioType.lower() == 'song':
        req = {k: v for k, v in req.dict().items() if v is not None}
        updated_audio = await update_song(id, req)
        if updated_audio:
            return ResponseModel(
                "Audio with ID: {} name update is successful".format(id),
                "Audio name updated successfully",
            )
    elif audioType.lower() == 'podcast':
        req = {k: v for k, v in req.dict().items() if v is not None}
        updated_audio = await update_podcast(id, req)
        if updated_audio:
            return ResponseModel(
                "Audio with ID: {} name update is successful".format(id),
                "Audio name updated successfully",
            )
    elif audioType.lower() == 'audiobook':
        req = {k: v for k, v in req.dict().items() if v is not None}
        updated_audio = await update_audiobook(id, req)
        if updated_audio:
            return ResponseModel(
                "Audio with ID: {} name update is successful".format(id),
                "Audio name updated successfully",
            )
    return ErrorResponseModel(
        "An error occurred",
        400,
        "There was an error updating the Audio data.",
    )
