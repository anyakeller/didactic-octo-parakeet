from pymongo import MongoClient
import csv

def init_db():
    c = MongoClient("lisa.stuy.edu",27017)
    db = c["meme-team-lite"]
    
    courses = csv.DictReader(open("courses.csv"))
    peeps = csv.DictReader(open("peeps.csv"))

    studentDict = {}

    for peep in peeps:
	peep["classes"] = []
	studentDict[peep["id"]] =  peep

    for course in courses:
	if course["id"] in studentDict:
	    studentDict[course["id"]]["classes"].append(course)
	
    for student in studentDict:
        db.students.insert_one(studentDict[student])

init_db()
