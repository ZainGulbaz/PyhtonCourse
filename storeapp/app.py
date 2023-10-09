from flask import Flask,request;

app=Flask(__name__);

stores=[
    {
       "name":"Dominos",
       "items":[
           {
               "name":"Pizza",
               "price":400
           },
           {
               "name":"coke",
               "price":150
           }
       ] 
    }
]

#Reading the stores
@app.get("/store")
def getStores():
    return stores;

#Create a store
@app.post("/store")
def createStore():
    store= request.json;
    stores.append(store);

    return {"message":"The store has been created successfully"};

