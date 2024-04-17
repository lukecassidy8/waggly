from azure.cosmos import CosmosClient, exceptions, PartitionKey
import json
import asyncio
from os import getenv
import logging

uri = getenv('uri')
key = getenv('key')
client = CosmosClient(uri, credential=key)
databaseName = 'users'
database = client.get_database_client(databaseName)
containerName = 'registry'
container = database.get_container_client(containerName)
logging.getLogger('azure').setLevel(logging.WARNING)
#Create the database
# try:
#     database = client.create_database(databaseName)
# except exceptions.CosmosResourceExistsError:
#     database = client.get_database_client(databaseName)

# Create container
# try: 
#     container = database.create_container(id=containerName, partition_key=PartitionKey(path='/username', kind='Hash'))
# except exceptions.CosmosResourceExistError:
#     container = database.get_container_client(containerName)
# except exceptions.CosmosHttpResponseError:
#     raise

def insertUser(username, password, userType):
    try:
        user_document = {
            'id': username,  # Use username as the 'id'
            'username': username,
            'password': password,
            'userType': userType
        }
        container.create_item(body=user_document)
    except exceptions.CosmosHttpResponseError as e:
        logging.error('Error inserting into cosmosdb')

def authenticateUser(username, password):
    loginQuery = f"SELECT * FROM c WHERE c.username = '{username}' AND c.password = '{password}'"
    items = list(container.query_items(query=loginQuery, enable_cross_partition_query=True))
    if items:
        return items[0]['userType']
    else:
        return None