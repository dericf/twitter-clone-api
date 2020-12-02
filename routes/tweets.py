from flask import request, jsonify, Response
from application import app

import db
import utils

@app.route("/api/tweets", methods=["GET"])
def tweets_get():
	return_data = []
	userId = request.args.get("userId")

	query =f"""SELECT tweets.id, tweets.content, users.id, username 
	FROM tweets 
	INNER JOIN users ON tweets.user_id=users.id 
	{'WHERE tweets.user_id=?' if userId else ""}"""
	print(query)
	success, tweets = db.get_all(query, (userId,) if userId else ())
	# print("tweets")
	# print(tweets)
	if success:
		for tweet in tweets:
			return_data.append({ 
					"tweetId": tweet[0],
					"userId": tweet[2],
					"username": tweet[3],
					"content": tweet[1],
					"createdAt": "0000-00-00"
			})
	return jsonify(return_data)


@app.route("/api/tweets", methods=["POST"])
def tweets_post():
	"""Expected Data:
	loginToken: string - jwt
	content: string
	"""
	return_data = []
	response_code = 201
	login_token = utils.decode_login_token(request.json.get('loginToken'))
	user_id = login_token.get("userId")
	content = request.json.get("content")

	if not user_id:
		return jsonify({"status": "error", "message":"Invalid user Id"})
	if not content:
		return jsonify({"status": "error", "message":"Invalid Content"})
	query ="""INSERT INTO tweets (user_id, content) VALUES (?,?)"""
	success, tweet_id = db.insert_one(query, (user_id, content))

	if success:
		return_data.append({ 
				"userId": user_id,
				"tweetId": tweet_id,
				"username": login_token.get("username"),
				"content": content,
				"createdAt": "0000-00-00"
		})
	return jsonify(return_data), response_code


@app.route("/api/tweets", methods=["PATCH"])
def tweets_patch():
	return_data = []
	response_code = 500

	login_token = utils.decode_login_token(request.json.get('loginToken'))
	user_id = login_token.get("userId")
	content = request.json.get("content")
	tweet_id = request.json.get("tweetId")
	
	# First get the tweet so we can check the user owns it
	success, tweet = db.get_one("SELECT id, user_id FROM tweets WHERE id=?", (tweet_id,))

	if tweet is None:
		return jsonify({"status": "error", "message":"Invalid tweetId was passed"}), 500

	if not success or (not user_id):
		response_code = 500
		return jsonify({"status": "error", "message":"Invalid user Id"}), response_code
	
	if user_id != tweet[1]:
		response_code = 500
		return jsonify({"status": "error", "message":"Cannot edit another user's tweet"}), response_code

	success = db.update_one("UPDATE tweets SET content=? WHERE id=?", (content, tweet_id))
	
	if success:
		return_data.append({ 
				"tweetId": tweet_id,
				"content": content,
		})
	else:
		response_code = 500
	return jsonify(return_data), response_code


@app.route("/api/tweets", methods=["DELETE"])
def tweets_delete():
	return_data = None
	response_code = 200
	login_token = utils.decode_login_token(request.json.get('loginToken'))
	user_id = login_token.get("userId")
	tweet_id = request.json.get("tweetId")

	if not tweet_id:
		return jsonify({"status": "error", "message":"Invalid tweet Id"})

	success, tweet = db.get_one("SELECT id, user_id FROM tweets WHERE id=?", (tweet_id,))

	if success and tweet[1] == user_id:
		db.delete_one("DELETE FROM tweets WHERE id=?", (tweet_id,))
			
	else:
		response_code = 500

	return jsonify(return_data), response_code