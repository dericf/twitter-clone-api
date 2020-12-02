from flask import request, jsonify, Response
from application import app

import db
import utils

@app.route("/api/followers", methods=["GET"])
def followers_get():
	return_data = []
	userId = request.args.get("userId")

	if not userId:
		return jsonify({"status": "error", "message":"Invalid user Id"})
	query ="""SELECT follows.id, users.id, email, username, bio 
	FROM follows 
	INNER JOIN users ON follows.user_id=users.id 
	WHERE follows.follows_user_id=?"""
	success, followers = db.get_all(query, (userId,))
	# print("followers")
	# print(followers)
	if success:
		for user in followers:
			return_data.append({ 
					"userId": user[1],
					"email": user[2],
					"username": user[3],
					"bio": user[4],
					"birthdate": "0000-00-00"
			})
	return jsonify(return_data)