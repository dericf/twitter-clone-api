'''
docs: "./documentation/follows.md"
'''

from flask import request, jsonify, Response
from application import app

import db
import utils


@app.route('/api/follows', methods=['GET'])
def follows_get():
    if request.method == 'GET':
        user_id = request.args.get("userId")
        response_data = []
        if user_id:
            success, follows = db.get_all(
                "SELECT follows.user_id, follows.follows_user_id, user.id, user.email, user.username, user.bio FROM follows INNER JOIN users AS user ON user.id=follows.follows_user_id WHERE follows.user_id=?", (int(user_id),))
            print(list(follows))
            for user in follows:
              response_data.append({
                  "userId": user[0],
                  "email": user[1],
                  "username": user[2],
                  "bio": user[3],
                  "birthdate": "0000-00-00"

              })

            if success :
              return jsonify(response_data) 
            else:
              return {"STATUS": "ERROR"}, 500


@app.route('/api/follows', methods=['POST'])
def follows_post():
    if request.method == 'POST':
        login_token = utils.decode_login_token(request.json.get("loginToken"))
        user_id = login_token['userId']
        
        follow_id = request.json.get('followId')
        # Todo: Before inserting - check if follow relationship already exists
        success = db.insert_one(
            "INSERT INTO follows (user_id, follows_user_id) VALUES(?,?)", (user_id, follow_id))
        if success:
            return_data = None

            return Response()
        else:
            return {"STATUS": "ERROR"}, 500


@app.route('/api/follows', methods=['DELETE'])
def follows_delete():
    if request.method == 'DELETE':
        # delete follow relationship (un-follow a user)
        login_token = utils.decode_login_token(request.json.get("loginToken"))
        user_id = login_token['userId']
        follow_id = request.json.get('followId')

        if user_id and follow_id:
          db.delete_one("DELETE FROM follows WHERE user_id=? AND follows_user_id=?", (user_id, follow_id))
          db.delete_one("DELETE FROM follows WHERE id=?", (int(user_id),))
          return {}, 204
        else:
          return {"STATUS": "ERROR"}, 500
