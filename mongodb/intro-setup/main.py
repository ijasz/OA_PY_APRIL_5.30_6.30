from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId



uri = "mongodb+srv://root:mCEqu3blkTNdMceK@realmcluster.zmek8.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

# show db
# print(client.list_databases())

# for i in client.list_databases():
#     print(i)\

# create db
db = client["OA-PY-5-30-6-30"]
db2 = client["OA-PY-5-30-6-30"]

# create collection
user = db['user']

# user.insert_one({"name": "ocean", "age": 20, "location": "pondy"})

# collection of data

# data = [
#     {"name": "river", "age": 25, "location": "coast"},
#     {"name": "forest", "age": 18, "location": "woods"},
#     {"name": "mountain", "age": 30, "location": "peak"},
#     {"name": "valley", "age": 22, "location": "meadow"},
#     {"name": "desert", "age": 27, "location": "dunes"},
#     {"name": "lake", "age": 19, "location": "shore"},
#     {"name": "cave", "age": 21, "location": "underground"},
#     {"name": "island", "age": 28, "location": "ocean"},
#     {"name": "creek", "age": 24, "location": "forest"},
#     {"name": "glacier", "age": 26, "location": "ice"},
#     {"name": "spring", "age": 23, "location": "meadow"}
# ]


# user.insert_many(data)

# read

# query = {"_id" : ObjectId('6474a3e8c57b61601fd0b2eb')}
# field = {"_id" : 0, "age" : 1}

# findone = user.find_one(query, field)

query = {"location" : "pondy"}
field = {"_id" : 0, "age" : 1}

find = user.find(query, field)

for i in find:
    print(i)

# print(find)


