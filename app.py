from flask import Flask, render_template, url_for, request, jsonify
from models.user_model import UserModel
from query_engine import db_create_user


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/create_user')
def create_user():
    payload = request.get_json()
    print(payload)
    if "id" in payload:
        payload.pop("id")
    status = UserModel.validate(payload, partial=("id",))
    print(status)
    if status:
        return jsonify(status), 400
    user = UserModel.from_dict(payload)
    print(user)
    db_create_user(user)
    return jsonify(data=user.to_dict()), 201
