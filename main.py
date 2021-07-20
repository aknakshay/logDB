from flask import Flask, request
from adb.ADB import ADB
import json

app = Flask("ADB Engine")
db = ADB()


@app.route("/", methods=['POST', 'GET'])
def post():
    if request.method == "POST":
        data = json.loads(request.data)
        key = data['key']
        value = data['value']
        db.set(key, value)
        return "200"
    elif request.method == "GET":
        try:
            tmp = request.data
            data = json.loads(tmp)
        except:
            print("No data passed")
            return "Log DB! v 0.1 \n Designed in WBAA Accelerator"
        try:
            key = data['key']
            return db.get(key)
        except:
            return "No Key Found"


if __name__ == "__main__":
    app.run(host='0.0.0.0')  # run the flask app
