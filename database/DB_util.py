from pymongo import MongoClient

client = MongoClient("localhost", 27017, maxPoolSize=50)


class MongoDB:
    __instance = None
    db = None
    @staticmethod
    def getInstance():
        """ Static access method. """
        if MongoDB.__instance == None:
            MongoDB()
        return MongoDB.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if MongoDB.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            MongoDB.db = client.covid19
            MongoDB.__instance = self

    def create_document(self, doc, collection_name):
        try:
            MongoDB.db.collection_name.insert(doc)
        except Exception as err:
            print(err)

    def create_docs(self, docs, collection_name):
        try:
            if collection_name == "current_situation":
                MongoDB.db.current_situation.insert_many(docs)
        except Exception as err:
            print(err)
