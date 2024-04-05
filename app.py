from flask import Flask, render_template, request, jsonify
import db_crud

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register.html', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def registerUser():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    userType = data.get('userType')

    db_crud.insertUser(username, password, userType)

    return jsonify({'message': 'Registration successful'})


if __name__ == '__main__':
    app.run(debug=True)
