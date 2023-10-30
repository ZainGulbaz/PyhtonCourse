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


#Create the stores
@app.post("/store")
def createStore():
    store=request.json;
    stores.append(store);
    return {"message":"The store has been created"},254;


#Give us a store on the basis of id

# FE -> req he wants a store with id 0 -> return store with id 0

# Path parameter

@app.get("/store/<string:storeId>")
def getStoreById(storeId):
    if(int(storeId) >= len(stores)):
        return {"error":"The id provided is not valid"},404;
    return stores[int(storeId)];
