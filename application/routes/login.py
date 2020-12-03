from flask import request, jsonify
from application import app
import db
import utils

@app.route('/api/login', methods=['POST'])
def login_post():
    if request.method == 'POST':
        email = request.json.get('email')
        password = request.json.get('password')
        #
        # Try and get the user
        #
        success, user = db.get_user_by_email(email)
        print("User", user)

        if not user:
            return jsonify({"status": "error", "message":"No user with that email exists"}), 500
        #
        # Check if passwords match
        #
        if not utils.check_password(password, user[4]):
            return jsonify({"status": "error", "message":"Passwords do not match"}), 500
        #
        # Generate the  login token
        #
        login_token = utils.generate_login_token(user[0], user[1])
        print("login token", type(login_token))
        status = db.insert_one(
            "INSERT INTO sessions (user_id, token) VALUES(?,?)", (user[0], login_token))
        
        return_data = {
            "userId": user[0],
            "username": user[1],
            "email": user[2],
            "bio": user[3],
            "birthdate": user[5],
            "loginToken": login_token
        }

        return jsonify(return_data), 201


@app.route('/api/login', methods=['DELETE'])
def login_delete():
    if request.method == 'DELETE':
        encoded_login_token = request.json.get("loginToken")
        login_token = utils.decode_login_token(encoded_login_token)
        user_id = login_token['userId']
        
        # delete the session
        if user_id:
            db.delete_one("DELETE FROM sessions WHERE token=? and user_id=?", (encoded_login_token, user_id))
            return "", 204
        else:
            return {"status": "error"}, 500
