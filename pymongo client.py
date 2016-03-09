from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.test

post1 = {"x": 10}
post2 = {"y": 20}

posts = db.posts

post_id = posts.insert_one(post1)
print(post_id)
post_id = posts.insert_one(post2)

posts.find_one()

print(232)

