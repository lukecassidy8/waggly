from pymongo import MongoClient

def createConnection(connectionString) -> MongoClient:
    try:
        client = MongoClient(connectionString)
        print(client.server_info())
        return client
    except Exception as e:
        return str(e)