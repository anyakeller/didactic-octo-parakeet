from pymongo import MongoClient

def getData():
    c = MongoClient("lisa.stuy.edu",27017)
    print MongoClient.find()

getData()
