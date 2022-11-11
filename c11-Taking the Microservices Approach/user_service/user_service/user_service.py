'''
File: user_service.py
Description: The user management service
Author: Saurabh Badhwar
'''
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import secrets

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

db = SQLAlchemy(app)

from user_service.models import User, Token

def check_required_fields(req_fields, input_list):
    """Check if the required fields are present or not in a given list.

    Keyword arguments:
    req_fields -- The list of fields required
    input_list -- The input list to check for

    Returns:
        Boolean
    """

    if all(field in req_fields for field in input_list):
        return True
    return False

@app.route('/ping', methods=['GET'])
def ping():
    """Ping application route."""
    return "PONG"

@app.route('/auth/register', methods=['POST'])
def user_registration():
    """Handle the user registration."""
    
    required_fields = ['username', 'email', 'password']
    response = {} # Initialize a response dictionary
    user_data = request.get_json()
    print(user_data)
    type(user_data)
    if not check_required_fields(required_fields, user_data.keys()):
        response['message'] = "Required fields are missing"
        return jsonify(response), 400

    # Create a user object
    username = user_data['username']
    password = generate_password_hash(user_data['password'])
    email = user_data['email']

    user = User(username=username, password=password, email=email)
    db.session.add(user)
    try:
        db.session.commit()
    except Exception:
        response['message'] = 'Unable to register the user'
        return jsonify(response), 400

    response['message'] = "User registration successful"
    return jsonify(response), 200

@app.route('/auth/login', methods=['POST'])
def user_login():
    """Handle the user login."""

    required_fields = ['username', 'password']
    response = {}
    user_data = request.get_json()
    if not check_required_fields(required_fields, user_data.keys()):
        response['message'] = "Username or password is incorrect"
        return jsonify(response), 400

    username = user_data['username']
    password = user_data['password']
    user = User.query.filter_by(username=username).first()

    if check_password_hash(user.password, password):
        # Create a new token and store it
        auth_token = secrets.token_hex(64)
        token = Token(user_id=user.id, auth_token=auth_token)
        db.session.add(token)
        try:
            db.session.commit()
        except Exception:
            response['message'] = "Unable to generate an authentication token"
            return jsonify(response), 500

        response['token'] = auth_token
        return jsonify(response), 200

@app.route('/auth/validate', methods=['POST'])
def validate_token():
    """Handle the validation of the token."""

    required_fields = ['auth_token']
    response = {}
    user_data = request.get_json()

    if not check_required_fields(required_fields, user_data.keys()):
        response['message'] = "Please provide a valid token"
        return jsonify(response), 400

    auth_token = user_data['auth_token']
    token = Token.query.filter_by(auth_token=auth_token).first()

    if token is None:
        response['message'] = "Invalid token provided"
        return jsonify(response), 400

    current_time = datetime.datetime.now()
    if (current_time - token.token_timestamp).total_seconds() >= 3600:
        db.session.delete(token)
        try:
            db.session.commit()
        except Exception:
            response['message'] = "Unable to authenticate token"
            return jsonify(response), 500
        response['message'] = "Token has expired. Please re-login."
        return jsonify(response), 401

    # we have the token authenticated, return the user id
    user = User.query.filter_by(id=token.user_id).first()
    user_id = user.id
    response['user_id'] = user_id

    return jsonify(response), 200

