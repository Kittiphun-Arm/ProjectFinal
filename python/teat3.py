import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:68276728@projectdisasterrisk.wh8co.gcp.mongodb.net/DATAPROJECT?retryWrites=true&w=majority")
db = client.test
col = db["testcollection"]
col.insert_one({"data1":"1","data2":"2"})