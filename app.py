from flask import Flask, render_template, request, jsonify
from db import createConnection

app = Flask(__name__)

connectionString = "mongodb://waggly-main-users-db:PxfLHSJwuGt9eRWw81Ow5cRFt2Vah60pg44C3nDxZ80J6yUZxbhrwLGhxfTs31uHC64TrI8IL7yJACDbzMYvWw==@waggly-main-users-db.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@waggly-main-users-db@"

connectionResult = createConnection(connectionString) # Client Object
# db = createConnection["users"] # DB Object
# collection_one = db["registry"] # Collection


# Routes
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register.html')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
