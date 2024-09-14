from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask

app = Flask(__name__)

uri = "mongodb+srv://stonew9799:0JkLuIc2ThPExqyk@hophack-cluster.ulbgg.mongodb.net/?retryWrites=true&w=majority&appName=hophack-cluster"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.your_database
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)