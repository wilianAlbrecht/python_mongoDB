from typing import Dict, List

class Teste_collection_repository:

    def __init__(self, db_connection) -> None:
        self.__collection_name = "teste_collection"
        self.__db_connection = db_connection

    def insert_documents(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document
    
    def insert_list_of_documents(self, list_of_documents: List[Dict]) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)
        return list_of_documents
    
    def select_many(self, filtro: Dict) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filtro, {"address" : 0, "_id": 0})
        return data
    
    def select_if_property_exist(self, filtro) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({filtro: { "$exists": True}}, {"address" : 0, "_id": 0})
        return data
    

