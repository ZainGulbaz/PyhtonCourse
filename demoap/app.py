#1 import flask library

from flask import Flask;

#Create an application

app= Flask(__name__);

#Declare the api type

@app.route("/api")
def getData():
    return {"store":"Dominos"}