from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

conn = MongoClient("mongodb+srv://atulsharma28092002:Atul2345@myfirstapi.oyvbxbe.mongodb.net/")

def convert_object_id(data):
    if isinstance(data, ObjectId):
        return str(data)
    if isinstance(data, list):
        return [convert_object_id(item) for item in data]
    if isinstance(data, dict):
        return {key: convert_object_id(value) for key, value in data.items()}
    return data

@app.get("/", response_class=JSONResponse)
async def read_item(request: Request):
    mydata = conn.myfirstApi.api1.find({})
    newdata = []
    for data in mydata:
        data = convert_object_id(data)  # Convert ObjectId to string
        newdata.append({
            "id": data.get("_id"),
            "mvid": data.get("mvid"),
            "Movie": data.get("Movie"),
            "Year": data.get("Year"),
            "Genre": data.get("Genre"),
            "Director": data.get("Director"),
            "Actor": data.get("Actor"),
            "Description": data.get("Description"),
            "Category": data.get("Category")
        })
    return JSONResponse(content=newdata)