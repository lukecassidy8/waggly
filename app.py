# app.py

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()