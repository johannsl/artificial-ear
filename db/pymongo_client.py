from pymongo import MongoClient
    

def connect_local():
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

def updateOne(songname, attribute, value):
    result = mc.update_one(
        {"Name": songname},
        {
            "$set": {
                attribute: value
                }
            }
        )
    return result

def deleteOne(songname):
    result = mc.remove({"Name": songname})

def findSongsByAttribute(attribute, value):
    songs = mc.find({attribute: value})
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

updateOne("posoo", "Key", "F")
deleteOne("hksdhas")

findAllSongs()

mc.remove()




