from pymongo import MongoClient
    

def connect_local():
    global db
    global client
    client = MongoClient("localhost", 27017)
    db = client.music
    client.close()

def disconnect():
    client.close()

def insert_one(songname, length, bpm, key):
    result = db.test.insert_one(
        {"Name": songname,
         "Length": length,
         "Tempo": bpm,
         "Key": key
         }
        )
    return result

connect_local()
    
insert_one("hksdhas", 140, 120, "C")
insert_one("asfasda", 155, 150, "A")
insert_one("asfasda", 185, 90, "G")

db.test.remove()
print(db.test.find_one())


