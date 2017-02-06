from pymongo import MongoClient

def getData():
    c = MongoClient("lisa.stuy.edu",27017)
    db = c["meme-team-lite"]
    studentsInfo = db.students.find()
    for student in studentsInfo:
	total = 0
	numClasses = 0
	for course in student["classes"]:
	    total += int(course["mark"])
	    numClasses += 1
	print "Student Name: " + student["name"]
        print "Average: " 
	print (total/numClasses)   

getData()
