from flask import request, jsonify
from application import app
import db
import utils

@app.route('/api/login', methods=['POST'])
def login_post():
    if request.method == 'POST':
        email = request.json.get('email')
        password = request.json.get('password')
        success, user = db.get_user_by_email(email)
        login_token = utils.generate_login_token(user[0], user[1])
        if user:
          if utils.check_password(password, user[4]):
              # sucess
              status = db.insert_one(
                  "INSERT INTO sessions (user_id, token) VALUES(?,?)", (user[0], login_token))
              print(status)  
              return_data = {
                  "userId": user[0],
                  "username": user[1],
                  "email": user[2],
                  "bio": user[3],
                  "birthdate": "000-00-00",
                  "loginToken": login_token
              }

              return return_data, 201
              
        return {"STATUS": "ERROR"}, 500


@app.route('/api/login', methods=['DELETE'])
def login_delete():
    if request.method == 'DELETE':
        encoded_login_token = request.json.get("loginToken")
        login_token = utils.decode_login_token(encoded_login_token)
        user_id = login_token['userId']
        print(login_token, user_id)
        # delete the session
        if user_id:
            db.delete_one("DELETE FROM sessions WHERE token=? and user_id=?", (encoded_login_token, user_id))
            return "<pre>{}</pre>", 204
        else:
            return {"STATUS": "ERROR"}, 500
