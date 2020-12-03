from flask import request, jsonify, Response
from application import app

import db
import utils

@app.route("/api/comments", methods=["GET"])
def comments_get():
	return_data = []
	tweet_id = request.args.get("tweetId")
	if tweet_id:
		#
		# first check if tweetId is valid
		#
		success, tweet = db.get_one("SELECT id FROM tweets WHERE id=?", (tweet_id,))
		if success and not tweet:
			return jsonify({"status": "error", "message":"Invalid Tweet Id"})
	query =f"""SELECT comments.id, comments.content, comments.created_at, users.id, username 
	FROM comments 
	INNER JOIN users ON comments.user_id=users.id 
	{'WHERE comments.tweet_id=?' if tweet_id else ""}"""
	print(query)
	success, comments = db.get_all(query, (tweet_id,) if tweet_id else ())
	# print("comments")
	# print(comments)
	if success:
		for comment in comments:
			return_data.append({ 
					"commentId": comment[0],
					"content": comment[1],
					"createdAt": comment[2],
					"userId": comment[3],
					"username": comment[4]
			})
	return jsonify(return_data), 200


@app.route("/api/comments", methods=["POST"])
def comments_post():
	"""Expected Data:
	loginToken: string - jwt
	content: string
	"""
	return_data = []
	response_code = 201
	#
	# Get all data from request body (JSON)
	#
	login_token = utils.decode_login_token(request.json.get('loginToken'))
	user_id = login_token.get("userId")
	username = login_token.get("username")
	content = request.json.get("content")
	tweet_id = request.json.get("tweetId")
	#
	# Validate
	# 
	if not user_id:
		return jsonify({"status": "error", "message":"Invalid Login Token"})
	if not content:
		return jsonify({"status": "error", "message":"No content provided"})
	elif content and len(content) > 150:
		return jsonify({"status": "error", "message":"Content exceeds 150 character limit"})

	query ="""INSERT INTO comments (user_id, tweet_id, content, created_at) VALUES (?,?,?, date('now'))"""
	success, comment_id = db.insert_one(query, (user_id, tweet_id, content))

	_, comment = db.get_one("SELECT created_at FROM comments WHERE id=?", (comment_id,))

	if success:
		return_data.append({ 
				"userId": user_id,
				"tweetId": tweet_id,
				"commentId": comment_id,
				"username": login_token.get("username"),
				"content": content,
				"createdAt": comment[0]
		})
	return jsonify(return_data), response_code


@app.route("/api/comments", methods=["PATCH"])
def comments_patch():
	return_data = []
	response_code = 200
	#
	# Get all data from request body (JSON)
	#
	login_token = utils.decode_login_token(request.json.get('loginToken'))
	user_id = login_token.get("userId")
	username = login_token.get("username")
	content = request.json.get("content")
	comment_id = request.json.get("commentId")
	
	# First get the comment so we can check the user owns it
	success, comment = db.get_one("SELECT id, user_id, tweet_id, created_at FROM comments WHERE id=?", (comment_id,))

	if not comment:
		return jsonify({"status": "error", "message":"Invalid commentId was passed"}), 500

	if not content:
		return jsonify({"status": "error", "message":"No content provided"})

	elif len(content) > 150:
		return jsonify({"status": "error", "message":"Content exceeds 150 character limit"})

	if not success or not user_id:
		response_code = 500
		return jsonify({"status": "error", "message":"Invalid user Id"}), response_code
	
	if user_id != comment[1]:
		response_code = 500
		return jsonify({"status": "error", "message":"Cannot edit another user's comment"}), response_code

	success = db.update_one("UPDATE comments SET content=? WHERE id=?", (content, comment_id))
	
	if success:
		return_data.append({ 
				"commentId": comment_id,
				"tweetId": comment[2],
				"userId": user_id,
				"username": login_token.get('username'),
				"content": content,
				"createdAt": comment[3],
		})
	else:
		response_code = 500
	return jsonify(return_data), response_code


@app.route("/api/comments", methods=["DELETE"])
def comments_delete():
	return_data = None
	response_code = 200
	login_token = utils.decode_login_token(request.json.get('loginToken'))
	user_id = login_token.get("userId")
	comment_id = request.json.get("commentId")

	success, comment = db.get_one("SELECT id, user_id FROM comments WHERE id=?", (comment_id,))

	if not success or not comment_id or not comment:
		return jsonify({"status": "error", "message":"Invalid comment Id"})

	if success and comment[1] != user_id:
			return jsonify({"status": "error", "message":"User does not own that comment"})
	#
	# OK to Delete Comment
	#
	db.delete_one("DELETE FROM comments WHERE id=?", (comment_id,))
	
	return '', 204