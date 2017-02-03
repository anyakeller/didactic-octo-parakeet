from pymongo import MongoClient
import csv

def init_db():
    c = MongoClient("lisa.stuy.edu",27017)
    db = c["meme-team-lite"]
    
    with open("courses.csv","r") as fcourses:
        courses = csv.DictReader(fcourses)
    fcourses.closed

    db.courses.insert_many(courses)

    with open("peeps.csv","r") as fpeeps:
        peeps = csv.DictReader(fpeeps)
    fpeeps.closed

    db.peeps.insert_many(peeps)

    
