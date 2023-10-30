from flask import Flask, request;
import mysql.connector;

app=Flask(__name__);

mysql=mysql.connector.connect(host="localhost",user="root",password="root",database="school");

cursor= mysql.cursor(dictionary=True);

@app.post("/student")
def createStudent():
    cursor.execute("INSERT INTO student(name,age) VALUES(%s,%s); ", ["sara",18]);
    mysql.commit();
    cursor.close();
    return {"message":"created student successfully"}


@app.get("/student")
def getStudent():
    cursor.execute("SELECT * FROM student");
    students=cursor.fetchall();
    return students;

