from os import getenv
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

uri = "mongodb+srv://camerapanicle0l:" + getenv('MONGO_PW') + "@cluster0.ubqc0jy.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
# db = client.test

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)