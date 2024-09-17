from pymongo import MongoClient

connection_string = "mongodb://user:123@localhost:27017/?authSource=teste_db"

client = MongoClient(connection_string)
db_connection = client["teste_db"]

# print(db_connection)

collection = db_connection.get_collection("teste_collection")

print(collection)

search_filter = {"ola": "mundo"}

response = collection.find(search_filter)

print(response)

for r in response:
    print(r)

# collection.insert_one({
#     "Estou": "Inserindo",
#     "numeros": [123, 456, 789]
# })