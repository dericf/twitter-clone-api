from flask import request, jsonify, Response
from application import app

import db
import utils

@app.route("/api/comment-likes", methods=["GET"])
def comment_likes_get():
	return_data = []
	comment_id = request.args.get("commentId")
	
	if comment_id:
		#
		# Check if the comment actually exists
		#
		success, comment = db.get_one("SELECT id FROM comments WHERE id=?", (comment_id,))
		if success and not comment:
			return jsonify({"status": "error", "message":"Invalid comment Id"}), 500

	query =f"""SELECT comment_likes.comment_id, users.id, users.username 
	FROM comment_likes 
	INNER JOIN users ON comment_likes.user_id=users.id
	{'WHERE comment_likes.comment_id=?' if comment_id else ""}"""
	success, comment_likes = db.get_all(query, (comment_id,) if comment_id else ())
	# print("comment_likes")
	# print(comment_likes)
	if success:
		for comment_like in comment_likes:
			return_data.append({ 
					"commentId": comment_like[0],
					"userId": comment_like[1],
					"username": comment_like[2]
			})
	return jsonify(return_data), 200


@app.route("/api/comment-likes", methods=["POST"])
def comment_likes_post():
	"""Expected Data:
	loginToken: string - jwt
	content: string
	"""
	return_data = []
	response_code = 201
	login_token = utils.decode_login_token(request.json.get('loginToken'))
	user_id = login_token.get("userId")
	comment_id = request.json.get("commentId")

	success, comment = db.get_one("SELECT id FROM comments WHERE id=?", (comment_id,))

	if not comment_id or not comment:
		return jsonify({"status": "error", "message":"Invalid comment Id"}), 500
	if not user_id:
		return jsonify({"status": "error", "message":"Invalid User Id"}), 500
	
	# check if user has already liked that comment

	success, comment_like = db.get_one("SELECT id, user_id FROM comment_likes WHERE comment_id=? AND user_id=?", (comment_id, user_id))

	if success and comment_like:
		# User has already liked this comment
		return jsonify({"status": "error", "message":"User has already liked this comment"}), 500
	#
	# OK for user to like this comment now
	#
	query ="""INSERT INTO comment_likes (user_id, comment_id) VALUES (?,?)"""
	success, comment_id = db.insert_one(query, (user_id, comment_id))
	
	return '', response_code

#
# NO PATCH
#

@app.route("/api/comment-likes", methods=["DELETE"])
def comment_likes_delete():
	return_data = None
	response_code = 204
	login_token = utils.decode_login_token(request.json.get('loginToken'))
	user_id = login_token.get("userId")
	comment_id = request.json.get("commentId")

	success, comment = db.get_one("SELECT id, content FROM comments WHERE id=?", (comment_id,))
	
	if not comment_id or not comment:
		return jsonify({"status": "error", "message":"Invalid comment Id"})

	success, comment_like = db.get_one("SELECT id, user_id, comment_id FROM comment_likes WHERE comment_id=? AND user_id=?", (comment_id, user_id))

	if success and not comment_like:
		response_code = 500
		return jsonify({"status": "error", "message":"User has not liked this comment"})

	db.delete_one("DELETE FROM comment_likes WHERE comment_id=? AND user_id=?", (comment_id, user_id))

	return '', response_code