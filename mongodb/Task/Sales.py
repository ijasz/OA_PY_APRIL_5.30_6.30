from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId



uri = "mongodb+srv://ijass:YKiHtkyRQ1GPwBWO@ocean-class.mscbll9.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


# # access db / create db
db = client["sample_supplies"]

# # create collection
sales = db['sales']


id=input("Give me your ID:")
product=input("want to know what things yor bought ? Y/N")

# query = {"name" : "laptop"}
# find = sales.find(query)
query = {"_id" : ObjectId('5bd761dcae323e45a93ccfee')}
sales.insert_one({"name": "laptop", "price": 604.12, "quantity": "4"})

# for x in sales.find():
  # print(x)








    