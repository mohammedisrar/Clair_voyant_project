import model
from pymongo import MongoClient
import env_files
import json
from bson import ObjectId


file_loc = env_files.file_loc

taget_col = env_files.taget_col

results = model.dummy_model(file_loc ,taget_col)

model_loc = model.model_path

meta_data= {'local_csv':file_loc , 'model_loc' : file_loc , 
       'model_results':results , 'taget_col':taget_col}



client = MongoClient("mongodb+srv://mohammedisrar84:Boojaana786@cluster0.3rt4bqh.mongodb.net/")
db = client.get_database('clair_db')
records = db.tenant

records.insert_one(meta_data)
inserted_data = list(records.find())[-1]
