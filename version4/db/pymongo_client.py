from pymongo import MongoClient
    

def connect_local():
    global mc
    client = MongoClient('10.22.114.4', 27017)
    db = client.music
    mc = db.music_collection

def disconnect():
    client.close()

def insertOne(title, length, bpm, key):
    deleteOne(title)
    result = mc.insert_one(
        {"Title": title,
         "Length": length,
         "Tempo": bpm,
         "Key": key,
         }
        )
    return result

def updateAttribute(title, attribute, value):
    result = mc.update_one(
        {"Name": title},
        {
            "$set": {
                attribute: value
                }
            }
        )
    return result

def deleteOne(title):
    result = mc.remove({"Title": title})

def findSongsByAttribute(attribute, value):
    songs = mc.find({attribute: value})
    for song in songs:
        print(song.get("Title"))

def findAllSongs():
    songs = mc.find()
    for song in songs:
        tempo = str (song.get("Tempo"))
        print('title:' + song.get("Title") + ', tempo:' + tempo + ', key:' + song.get("Key"))







