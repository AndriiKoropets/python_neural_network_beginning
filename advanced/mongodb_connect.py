import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

print(myclient)
print(mydb.name)
print(mydb.list_collection_names())

collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")