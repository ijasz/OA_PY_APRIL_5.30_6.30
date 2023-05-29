from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:mCEqu3blkTNdMceK@realmcluster.zmek8.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


# create db
db = client["OA-PY-5-30-6-30"]
db2 = client["OA-PY-5-30-6-30"]

# create collection
user = db['user']

# user.insert_one({"name": "ocean", "age": 20, "location": "pondy"})

# collection of data

data = [
    {"name": "river", "age": 25, "location": "coast"},
    {"name": "forest", "age": 18, "location": "woods"},
    {"name": "mountain", "age": 30, "location": "peak"},
    {"name": "valley", "age": 22, "location": "meadow"},
    {"name": "desert", "age": 27, "location": "dunes"},
    {"name": "lake", "age": 19, "location": "shore"},
    {"name": "cave", "age": 21, "location": "underground"},
    {"name": "island", "age": 28, "location": "ocean"},
    {"name": "creek", "age": 24, "location": "forest"},
    {"name": "glacier", "age": 26, "location": "ice"},
    {"name": "spring", "age": 23, "location": "meadow"}
]


user.insert_many(data)

# print(client.list_databases())

# for i in client.list_databases():
#     print(i)
