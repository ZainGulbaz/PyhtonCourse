#create student, get students, give us student on the basis of name 
#Connect flask with the database
#mysql-connector-python
from flask import Flask, request;
import mysql.connector;

app= Flask(__name__);

connection = mysql.connector.connect(host="localhost",user="root",password="root",database="school");


@app.post("/student")
def create_student():
    body=request.json;
    cursor= connection.cursor();
    cursor.execute("INSERT INTO student(name,age) VALUES(%s,%s)",[body["name"],body["age"]]);
    connection.commit();
    cursor.close();
    return "Student is created";

@app.get("/student")
def getStudents():
    cursor=connection.cursor(dictionary=True);
    cursor.execute("SELECT * FROM student");
    students=cursor.fetchall();
    cursor.close();
    return students;



    





