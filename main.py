from fastapi import FastAPI
from typing import Optional
from typing import List


app = FastAPI()

students = {}

student_data = {"id": 0, "Name": "", "sex": "", "age": 0, "Height": 0, "email": ""}

@app.get("/")
def home():
    return "Hello, user welcome to my API"


@app.get("/students")
def get_students():
    return students

@app.post("/students")
def add_student(first_name: str, last_name: str, email: str, age: int, sex: str, Height: float):

    new_student = student_data.copy()
    new_student["id"] = len(students) + 1
    new_student["Name"] = first_name + " " + last_name
    new_student["email"] = email
    new_student["sex"] = sex
    new_student["age"] = age
    new_student["Height"] = Height
    students[new_student["id"]] = new_student

    return new_student

@app.get("/students/search/{id}")
def search_student(id: int,):
    if id in students:
        return students[id]
    else:
        return {"Error": "Student not found"}
    

@app.post("/students/{id}")
def search_students(ids: List[int]):
    result = []
    for id in ids:
        if id in students:
            result.append(students[id])
    if result:
        return result
    else:
        return {"Error": "Student(s) not found"}

@app.put("/students/{id}")
def update_student(id: int, first_name: Optional[str] = None, last_name: Optional[str] = None, email: Optional[str] = None, age: Optional[int] = None, sex: Optional[str] = None, Height: Optional[float] = None):
    if id not in students:
        return {"Error": "Student not found"}
    
    student = students[id]

    if first_name is not None:
        student["first_name"] = first_name
    if last_name is not None:
        student["last_name"] = last_name
    if email is not None:
        student["email"] = email
    if age is not None:
        student["age"] = age
    if sex is not None:
        student["sex"] = sex
    if Height is not None:
        student["Height"] = Height

    return student


@app.delete("/students/{id}")
def delete_student(id: int):
    if id in students:
        del students[id]
        return {"Message": "Student deleted"}
    else:
        return {"Error": "Student not found"}
    
    




    

    
         


    







