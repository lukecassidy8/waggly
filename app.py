# app.py

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run()
