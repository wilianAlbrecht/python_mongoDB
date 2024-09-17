from models.connection_options.connection import  DBConnectionHandler
from models.repositorys.teste_collection_repository import Teste_collection_repository

db_handle = DBConnectionHandler()
db_handle.connecy_to_db()
db_connection = db_handle.get_db_connection()

teste_collection_repository = Teste_collection_repository(db_connection)

order = {
    "name": "wilian",
    "address": "rua abacate",
    "order": {
        "pizza": "1",
        "coca": "2",
        "batata": "1"
    }
}

teste_collection_repository.insert_documents(order)

order_list = [{
    "name": "wilian",
    "address": "rua abacate",
    "order": {
        "pizza": "1",
        "coca": "2",
        "batata": "1"
    }
},
{
    "name": "jose",
    "address": "rua abacaxi",
    "order": {
        "sorvete": "2",
        "milkshake": "1"
    }
}

]

teste_collection_repository.insert_list_of_documents(order_list)