from pymongo import MongoClient

connection_string = "mongodb://root:root@localhost:27017/?authSource=admin"
client = MongoClient(connection_string)
db_connection = client["myBase"]

# print(db_connection)

collection = db_connection.get_collection("myCollection")

# print(collection)

search_filter = {"ola": "mundo"}

# response = collection.find(search_filter)

# print(response)

collection.insert_one({
    "Estou": "Inserindo",
    "numeros": [123, 456, 789]
})