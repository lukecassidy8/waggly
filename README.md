
# Project Setup Guide

## Installing VS Code and Extensions
1. Install Visual Studio Code (VS Code).
2. Open VS Code and navigate to the Extensions tab.
3. Install Git and Azure Tools library from the Extensions marketplace.

## Cloning Repository
1. Execute the following command to clone the repository
	- git clone https://github.com/lukecassidy8/waggly


## Setting Up Azure Resources
1. Log into portal.azure.com.
2. Create an Azure subscription and resource group.
3. In VS Code, navigate to the Azure icon on the left-hand side, and sign into Azure.
4. Click the down arrow next to the subscription.
5. Under the "App Services" tab, right-click and select "Create new Web App (Advanced)".
6. Select the created resource group, Python 3.9 as the runtime stack, and an app service plan.
7. Create a new application insights resource.
8. Once the web app is created, do not press deploy.

## Configuring Azure Cosmos DB
1. Navigate back to Azure Portal home and press "Create a resource".
2. Search for Azure CosmosDB and select "Create".
3. Choose Azure CosmosDB for NoSQL API.
4. Under the basics tab, select the same subscription and resource group.
5. Under the Basics tab, select provisioned throughput as the capacity mode.
6. Apply Free Tier Discount and create the resource.
7. Once deployed, navigate to the resource and copy the primary key and URI.
8. Create a file called `.env` in your VS Code project (add it to `.gitignore`).
9. Inside `.env`, create variables `uri` and `key` with values from the database in the following format:
	- uri="your URI" 
	- key="your key"
10. Uncomment lines 15-19 in `db_crud.py`, run the file, then re-comment those lines and uncomment lines 21-27. Run the file again.

## Dependencies and Virtual Environment
1. If errors persist, create a virtual environment and run:
	- pip install -r requirements.txt
2. Re-comment or delete lines 15-27 once the database is created and visible in Azure Portal.

## GitHub Repository
1. Commit and push the cloned code to a personal GitHub repository under the main branch.

## Configuring Azure Web App
1. Locate your created Azure Web App in the Azure Portal.
2. Navigate to the Configuration tab and go to General settings.
3. Paste the following custom start-up command:
	- gunicorn --bind=0.0.0.0 --timeout 600 startup:app
4. Save the settings.
5. Navigate to the Deployment Center tab.
6. Select GitHub under the source dropdown.
7. Choose the organization, repository, and branch.
8. Save the settings.
9. In GitHub, under the Actions tab, the pipeline should be building and deploying.

## Application Settings
1. Once deployed, navigate back to the Azure Web App.
2. Under Application settings, create two settings:
- `uri`: Add the URI from CosmosDB.
- `key`: Add the connection key from CosmosDB.

## Final Testing
1. Once the application is deployed, navigate to the URL created and shown in the Web App settings.
2. The application should all be working, including logging in and register
