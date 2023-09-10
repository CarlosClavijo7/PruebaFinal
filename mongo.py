
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://admin:Administrad0r@cluster0.mc2jx0g.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    print(client.list_database_names())
    db = client['Tratamiento_de_datos']

    col = db['PRUEBA']
    col.insert_one({
        'edad': 20
    })
except Exception as e:
    print(e)