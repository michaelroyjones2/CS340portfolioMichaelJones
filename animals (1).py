from pymongo import MongoClient

from bson.objectid import ObjectId

class AnimalShelter(object):

    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):

        # Initializing the MongoClient. This helps to 

        # access the MongoDB databases and collections. 

        self.client = MongoClient('mongodb://localhost:38026')

        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.

    def create(self, data):

        if data is not None:

            testInsert = self.database.animals.insert(data)  # data should be dictionary 
            print(testInsert)
           

        else:

            raise Exception("Nothing to save, because data parameter is empty")
            
    def read(self, data):

        if data is not None:

            testRead = self.database.animals.find(data)  # data should be dictionary 
            print(testRead)
            

        else:

            raise Exception("Nothing to save, because data parameter is empty")
            
    def update(self, data):
        if data is not None:
                
            testUpdate = self.database.animals.save(data)
            print(testUpdate)
                
        else:
                
            raise Exception("Nothing to save, because data parameter is empty")
            
    def delete(self, data):
        
        if data is not None:
            
            testDelete = self.database.animals.remove(data)
            print(testDelete)
            
        else:
            
            raise Exception("Nothing to save, because data parameter is empty")
                
                
    