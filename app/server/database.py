import motor.motor_asyncio
from bson.objectid import ObjectId
from datetime import datetime
# this is my monogodb uri you can use youre own mongodb uri if you want to see the data in mongodb atlas yourself.
MONGO_DETAILS = "mongodb+srv://ninja:ninja@cluster0.p8v6b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.audioserver
song_collection = database.get_collection("song_collection")
podcast_collection = database.get_collection("podcast_collection")
audiobook_collection = database.get_collection("audiobook_collection")
now = datetime.now()

# helpers


def song_helper(song) -> dict:
    return {
        "id": str(song["_id"]),
        "name": song["songmetadata"]["name"],
        "duration": song["songmetadata"]["duration"],
        "uploadedtime": song["songmetadata"]["uploadtime"],
    }


def podcast_helper(podcast) -> dict:
    return {
        "id": str(podcast["_id"]),
        "name": podcast["podcastmetadata"]["name"],
        "duration": podcast["podcastmetadata"]["duration"],
        "host": podcast["podcastmetadata"]["host"],
        "participants": podcast["podcastmetadata"]["participants"],
        "uploadedtime": podcast["podcastmetadata"]["uploadtime"],
    }


def audiobook_helper(audiobook) -> dict:
    return {
        "id": str(audiobook["_id"]),
        "title": audiobook["audiobookmetadata"]["title"],
        "author": audiobook["audiobookmetadata"]["author"],
        "narrator": audiobook["audiobookmetadata"]["narrator"],
        "duration": audiobook["audiobookmetadata"]["duration"],
        "uploadedtime": audiobook["audiobookmetadata"]["uploadtime"],
    }


async def add_song(song_data: dict) -> dict:
    song = await song_collection.insert_one(song_data)
    new_song = await song_collection.find_one({"_id": song.inserted_id})
    return song_helper(new_song)


async def add_podcast(podcast_data: dict) -> dict:
    podcast = await podcast_collection.insert_one(podcast_data)
    new_podcast = await podcast_collection.find_one({"_id": podcast.inserted_id})
    return podcast_helper(new_podcast)


async def add_audiobook(audiobook_data: dict) -> dict:
    audiobook = await audiobook_collection.insert_one(audiobook_data)
    new_audiobook = await audiobook_collection.find_one({"_id": audiobook.inserted_id})
    return audiobook_helper(new_audiobook)


async def retrieve_songs():
    songs = []
    async for song in song_collection.find():
        songs.append(song_helper(song))
    return songs


async def retrieve_podcasts():
    podcasts = []
    async for student in podcast_collection.find():
        podcasts.append(podcast_helper(student))
    return podcasts


async def retrieve_audiobooks():
    audiobooks = []
    async for audiobook in audiobook_collection.find():
        audiobooks.append(audiobook_helper(audiobook))
    return audiobooks


async def retrieve_song(id: str) -> dict:
    song = await song_collection.find_one({"_id": ObjectId(id)})
    if song:
        return song_helper(song)


async def retrieve_podcast(id: str) -> dict:
    podcast = await podcast_collection.find_one({"_id": ObjectId(id)})
    if podcast:
        return podcast_helper(podcast)


async def retrieve_audiobook(id: str) -> dict:
    audiobook = await audiobook_collection.find_one({"_id": ObjectId(id)})
    if audiobook:
        return audiobook_helper(audiobook)


async def delete_song(id: str):
    song = await song_collection.find_one({"_id": ObjectId(id)})
    if song:
        await song_collection.delete_one({"_id": ObjectId(id)})
        return True


async def delete_podcast(id: str):
    podcast = await podcast_collection.find_one({"_id": ObjectId(id)})
    if podcast:
        await podcast_collection.delete_one({"_id": ObjectId(id)})
        return True


async def delete_audiobook(id: str):
    audiobook = await audiobook_collection.find_one({"_id": ObjectId(id)})
    if audiobook:
        await audiobook_collection.delete_one({"_id": ObjectId(id)})
        return True


async def update_song(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    song = await song_collection.find_one({"_id": ObjectId(id)})
    if song:
        updated_song = await song_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_song:
            return True
        return False


async def update_podcast(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    podcast = await podcast_collection.find_one({"_id": ObjectId(id)})
    if podcast:
        updated_podcast = await podcast_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_podcast:
            return True
        return False


async def update_audiobook(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    audiobook = await audiobook_collection.find_one({"_id": ObjectId(id)})
    if audiobook:
        updated_audiobook = await audiobook_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_audiobook:
            return True
        return False
