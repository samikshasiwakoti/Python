student = {

    "name": "Samiksha",
    "age" : 23,
    "Location" : "jhapa"
}

print(student)
print(type(student))
print(student["name"])

# it can also conatin diffente data like int,float,strring,boolean,tuple,list and other dictionary

students = {
    "name": "Samiksha",
    "marks": 85.5,
    "subjects":["python","Django","sql"],
    "course":[" bca","csit","bba","bbs"]
}
students["marks"] = 80
print(students)
students["location"] = "jhapa"
print(students)
print(students["subjects"][0])
students["course"][0]= "bbm"
print(students)
print(students.get("name"))
print(students.keys())
print(students.values())
print(students.items())
student.pop('age')
print(student)
print("name" in students)
del student["Location"]
print(student)

# nested dictionaries
stu = {
    "Student1" :
    {
        "name":"samiksha",
        "age" : 23

    },
    "Student2":
    {
        "name":"Bhawana",
        "age": 22
    }
}
print(stu["Student1"]["name"])