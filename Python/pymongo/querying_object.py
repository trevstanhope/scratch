from pymongo import MongoClient
import datetime

client = MongoClient()
db = client['test-database']

# insert post
post = {"author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()}
posts = db.posts # the posts collection
post_id = posts.insert(post)

# collections
print db.collection_names()

# querying one doc
posts.find_one()
posts.find_one({"author": "Mike"})
posts.find_one({"_id": post_id})
post_id_as_str = str(post_id)
posts.find_one({"_id": post_id_as_str}) # No result

# Querying multiple docs
print posts.count()
print posts.find({"author": "Mike"}).count()
for post in posts.find():
    print post

# complex queries
d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
    print post
