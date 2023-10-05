from flask import Flask;

app= Flask(__name__);


@app.get("/api")
def getData():
    return { "name":"Zain Gulbaz" }
        
        
