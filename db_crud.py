from azure.cosmos import CosmosClient, exceptions, PartitionKey
from os import getenv
import logging
import random

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
        if userType == 'dogOwner':
            user_document['dogsOwned'] = random.randint(1,5)
        container.create_item(body=user_document)
    except exceptions.CosmosHttpResponseError as e:
        logging.error('Error inserting into cosmosdb')


def authenticateUser(username, password):
    logging.debug("db_crud.py: Checking credentials for username: %s", username)
    loginQuery = f"SELECT * FROM c WHERE c.username = '{username}' AND c.password = '{password}'"

    items = list(container.query_items(query=loginQuery, enable_cross_partition_query=True))

    if items:
        logging.debug("db_crud.py: Item retrieved from the database: %s", items[0])
        logging.debug("db_crud.py: Retrieving user type for username: %s", username)
        user_type = items[0].get('userType')
        logging.debug("db_crud.py: User type retrieved: %s", user_type)
        return user_type
    else:
        return None

def getNumberOfDogs(username):
    try:       
        getDogsQuery = f"SELECT c.dogsOwned FROM c WHERE c.username = '{username}'"
        items = list(container.query_items(query=getDogsQuery, enable_cross_partition_query=True))
        if items:
            return items[0].get('dogsOwned')
        else:
            return None
    except Exception as e:
        logging.error(f"Erorr getting number of dogs for user {username}: {str(e)}")
        return None