from flask import app, request, jsonify
from __main__ import app, db, utils


@app.route('/api/users', methods=['GET'])
def users_get():
    if request.method == 'GET':
        user_id = request.args.get("userId")
        response_data = []
        if user_id:
            success, user = db.get_one(
                "SELECT id as user_id, email, username, bio FROM users WHERE id=?", (int(user_id),))
            print(list(user))
            response_data.append({
                "userId": user[0],
                "email": user[1],
                "username": user[2],
                "bio": user[3],
                "birthdate": "0000-00-00"

            })

            return jsonify(response_data) if success else {"STATUS": "ERROR"}, 500
        else:
            success, users = db.get_all(
                "SELECT id as user_id, email, username, bio FROM users")
            for user in users:
                response_data.append({
                    "userId": user[0],
                    "email": user[1],
                    "username": user[2],
                    "bio": user[3],
                    "birthdate": "0000-00-00"
                })
            return jsonify(response_data) if success else {"STATUS": "ERROR"}, 500


@app.route('/api/users', methods=['POST'])
def users_post():
    if request.method == 'POST':
        email = request.json.get('email')
        password = request.json.get('password')
        username = request.json.get('username')
        bio = request.json.get('bio')

        p_hash = utils.hash_password(password)
        status = db.insert_one(
            "INSERT INTO users (email, password_hash, username, bio) VALUES(?,?,?,?)", (email, p_hash, username, bio))
        print(status)
        if status:
            success, user = db.get_user_by_email(email)
            return_data = { 
                "userId": user[0],
                "username": user[1],
                "email": user[2],
                "bio": user[3],
                "birthdate": "000-00-00",
                "loginToken": utils.generate_login_token(user[0])
            }

            return return_data
        else:
            return {"STATUS": "ERROR"}, 500


@app.route('/api/users', methods=['PATCH'])
def users_patch():
    if request.method == 'PATCH':
        # update user bio
        login_token = request.json.get("loginToken")
        return {"STATUS": "ERROR"}, 501


@app.route('/api/users', methods=['DELETE'])
def users_delete():
    if request.method == 'DELETE':
        # delete user
        login_token = utils.decode_login_token(request.json.get("loginToken"))
        user_id = login_token['userId']
        if user_id:
          db.delete_one("DELETE FROM users WHERE id=?", (int(user_id),))
          return {}, 200
        else:
          return {"STATUS": "ERROR"}, 500
