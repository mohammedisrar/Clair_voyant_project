from flask import Flask 
import metadata
import bson.json_util as json_util

app = Flask(__name__)

@app.route("/")
def func_1():
    existing_records = metadata.inserted_data
    print(existing_records)
    return json_util.dumps(existing_records)

if __name__ == "__main__":
    app.run()
    # hello world
