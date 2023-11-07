from os import getenv
from dotenv import load_dotenv
from pymongo import MongoClient
import sqlite3

load_dotenv()

uri = "mongodb+srv://camerapanicle0l:" + getenv('MONGO_PW') + "@cluster0.ubqc0jy.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

db = client.rpg

connection = sqlite3.connect('../rpg_db.sqlite3')

cursor = connection.cursor()

query = '''
SELECT * 
FROM armory_item as a
FULL JOIN armory_weapon as w
ON w.item_ptr_id = a.item_id
'''

item_d_list = [(x[0], {
                        "name": x[1],
                        "value": x[2],
                        "weight": x[3],
                        "power": x[5]
                      }
               ) for x in cursor.execute(query).fetchall()]

sql_id_to_mongo_id = {}
for item in item_d_list:
    inserted_item = db.items.insert_one(item[1])
    sql_id_to_mongo_id[item[0]] = inserted_item.inserted_id

query = '''
SELECT character_id, item_id
FROM charactercreator_character_inventory
'''

char_item_list = [(x[0], x[1]) for x in cursor.execute(query).fetchall()]

char_inventories = {}
for item in char_item_list:
    mongo_id = sql_id_to_mongo_id[item[1]]
    if item[0] in char_inventories:
        char_inventories[item[0]].append(mongo_id)
    else:
        char_inventories[item[0]] = [mongo_id]

query = '''
SELECT * 
FROM charactercreator_character
'''

characters = [(x[0], {
                        "name": x[1],
                        "level": x[2],
                        "exp": x[3],
                        "hp": x[4],
                        "strength": x[5],
                        "intelligence": x[6],
                        "dexterity": x[7],
                        "wisdom": x[8]
                     }
              ) for x in cursor.execute(query).fetchall()]

for char in characters:
    char_data = char[1]
    if char[0] in char_inventories:
        char_data["items"] = char_inventories[char[0]]
    db.characters.insert_one(char_data)