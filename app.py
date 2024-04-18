from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import db_crud
import secrets
import logging

app = Flask(__name__)
secretKey = secrets.token_hex(32)
app.secret_key = secretKey

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Routes
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register.html', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('index'))


@app.route('/getUserType')
def getUserType():
    if 'username' in session:
        username = session['username']
        logging.debug('App.py: User %s requested user type', username)
        
        userType = session.get('userType')
        if userType is not None:
            numberOfDogs = None
            if userType == 'dogOwner':
                numberOfDogs = db_crud.getNumberOfDogs(username)
            logging.info('App.py: User type for %s: %s', username, userType)
            return jsonify({'userType': userType, "numberOfDogs": numberOfDogs if numberOfDogs is not None else 0})
        else:
            logging.warning('App.py: User type not found for %s', username)
            return jsonify({'error': 'User type not found in session'})
    else:   
        logging.error('App.py: User not logged in')
        return jsonify({'error': 'User not logged in'})
    

@app.route('/login', methods=['POST'])
def loginUser():
    logging.debug('Received login request')
    logging.debug('Form data: %s', request.form)
    username = request.form['username']
    password = request.form['password']
    logging.debug('Username: %s', username)
    logging.debug('Password: %s', password)

    userType = db_crud.authenticateUser(username, password)
    if userType is not None:
        session['username'] = username
        session['userType'] = userType

        logging.info('User logged in successfully')
        return jsonify({'success': True, 'userType': userType})
    else:
        logging.warning('Invalid username or password')
        return jsonify({'success': False, 'message': 'Invalid username or password'})

@app.route('/register', methods=['POST'])
def registerUser():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    userType = data.get('userType')

    db_crud.insertUser(username, password, userType)

    return jsonify({'message': 'Registration successful'})


@app.route('/getNumberOfDogs')
def getNumberOfDogs():
    if 'username' in session:
        username = session['username']
        logging.debug('App.py: Retrieving number of dogs for user %s', username)

        numberOfDogs = db_crud.getNumberOfDogs(username)
        if numberOfDogs is not None:
            logging.info('App.py: Number of dogs for %s: %d', username, numberOfDogs)
            return jsonify({'numberOfDogs': numberOfDogs})
        else:
            logging.warning('App.py: Number of dogs not found for %s', username)
            return jsonify({'error': 'Number of dogs not found'})
    else:   
        logging.error('App.py: User not logged in')
        return jsonify({'error': 'User not logged in'})

@app.route('/logout')
def logoutUser():
    session.clear()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
