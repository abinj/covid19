from pymongo import MongoClient

client = MongoClient("localhost", 27017, maxPoolSize=50)
# db = client.covid19


class MongoDB:
   __instance = None
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
         MongoDB.__instance = client.covid19




