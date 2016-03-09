from pymongo import MongoClient
    

def connect_local():
    global db
    global client
    global mc
    client = MongoClient("localhost", 27017)
    db = client.music
    mc = db.music_collection

def disconnect():
    client.close()

def insertOne(songname, length, bpm, key):
    result = mc.insert_one(
        {"Name": songname,
         "Length": length,
         "Tempo": bpm,
         "Key": key
         }
        )
    return result

def findSongsByKey(key):
    songs = mc.find({"Key": key})
    for song in songs:
        print(song.get("Name"))

def findAllSongs():
    songs = mc.find()
    for song in songs:
        print(song.get("Name"))

connect_local()
    
insertOne("hksdhas", 140, 120, "C")
insertOne("hjhka", 135, 120, "C")
insertOne("asfasda", 155, 150, "A")
insertOne("posoo", 185, 90, "G")

findSongsByKey("G")

mc.remove()


