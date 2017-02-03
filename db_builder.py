from pymongo import MongoClient
import csv

def init_db():
    c = MongoClient("lisa.stuy.edu",27017)
    db = c["meme-team-lite"]
    
    courses = csv.DictReader(open("courses.csv"))
    peeps = csv.DictReader(open("peeps.csv"))

    db.courses.insert_many(courses)
    db.peeps.insert_many(peeps)

init_db()
