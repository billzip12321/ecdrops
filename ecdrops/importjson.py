import json
import pymongo

connection = pymongo.MongoClient("mongodb://localhost:27017")
db=connection.ecdrops
record=db.ecdrop
page = open(r'C:\Users\Administrator\ecdrops\brand.json','r')
parsed = json.loads(page.read())

for item in parsed["Records"]:
    record.insert(item)