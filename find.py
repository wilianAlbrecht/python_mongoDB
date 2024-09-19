from models.connection_options.connection import  DBConnectionHandler
from models.repositorys.teste_collection_repository import Teste_collection_repository

db_handle = DBConnectionHandler()
db_handle.connecy_to_db()
db_connection = db_handle.get_db_connection()

teste_collection_repository = Teste_collection_repository(db_connection)

filtro_select = {
    "name": "wilian"
}

result = teste_collection_repository.select_many(filtro_select)


print("")
print("                       select many")
print("")


for r in result:
    print(r)

print("-----------------------------------------------------------")


###########################################################################################


filtro_exist = "numeros"

result = teste_collection_repository.select_if_property_exist(filtro_exist)

print("")
print("                       select if property exists")
print("")

for r in result:
    print(r)


print("-----------------------------------------------------------")


###########################################################################################

# filtro_exist = "numeros"

# result = teste_collection_repository.select_if_property_exist(filtro_exist)

# print("")
# print("                       select many orders")
# print("")

# for r in result:
#     print(r)


# print("-----------------------------------------------------------")


###########################################################################################
