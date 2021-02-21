import pymongo


class Database(object):
    # no need for instance properties
    # class/static variables
    URI = 'mongodb://localhost:27017'
    DATABASE = None

    # method belongs to the class as a whole and not instance of it
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

