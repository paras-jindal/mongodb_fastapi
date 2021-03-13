import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://jaxene5847:test@cluster0.42bhf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

database = client.flask_mongodb

song_collection = database.get_collection("song")
audiobook_collection = database.get_collection("audiobook")
podcast_collection = database.get_collection("podcast")




