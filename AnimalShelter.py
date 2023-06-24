from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        USER = 'aacuser'
        PASS = 'Missy3434'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31977
        DB = 'AAC'
        COL = 'animals'
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert_one(data)  # data should be dictionary
            if insert != 0:
                return True
            else:
                raise Exception("Nothing to save, because data parameter is empty")

    # Complete this create method to implement the R in CRUD
    def read(self, criteria=None):
        if criteria is not None:
            data = self.database.animals.find_one(criteria, {"_id": False})
            for document in data:
                print(document)
                    
    def readAll(self, data):
        if data is not None:
            return self.database.animals.find(data,{"_id":False})
        else:
            raise Exception("nothing to read because data parameter is empty")

            
    # Complete to unplemnt the U in CRUD
    def update(self, searchData, updateData):
        if searchData is not None:
            result = self.database.animals.update_many(searchData, {"$set": updateData})
        else:
            return "{}"
        return result.raw_result 
    
    # Complete to implement the D in CRUD
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else:
            return "No document was found"
        return result.raw_result




# Create an instance of the AnimalShelter class
animals = AnimalShelter()
