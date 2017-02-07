from pymongo import MongoClient
import csv

def init_db():
    c = MongoClient("lisa.stuy.edu",27017)
    db = c["meme-team-lite"]
    
    teachers = csv.DictReader(open("teachers.csv"))

    teacherDict = {}

    for teacher in teachers:
	teacher["students"] = []
	teacherDict[teacher["code"]] = teacher

    studentsInfo = db.students.find()

    for student in studentsInfo:
        for course in student["classes"]:
	    teacherDict[course["code"]]["classes"].append(student["id"])
	
    for teacher in studentDict:
        db.teachers.insert_one(teacherDict[teacher])

init_db()
