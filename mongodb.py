import pymongo
client = pymongo.MongoClient("mongodb+srv://koffee:longlive007@testcluster.ahrh2.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
#data in bson format fed to mongoDB
d= {"name":"kunal","email":"kunalnayyar@gmail.com","surname":"nayyar"}
d1= {"name":"shadow","email":"shadznayyar@gmail.com","surname":"nayyar"}
d2= {"name":"simba","email":"simbsnayyar@gmail.com","surname":"nayyar"}

db1 = client['mongotest']
col1 = db1['test']
col1.insert_one(d)
col1.insert_many((d1,d2))