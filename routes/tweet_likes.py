from flask import request, jsonify, Response
from application import app

import db
import utils

@app.route("/api/tweet-likes", methods=["GET"])
def tweet_likes_get():
	return_data = []
	tweet_id = request.args.get("tweetId")
	
	query =f"""SELECT tweet_likes.id, users.id, users.username 
	FROM tweet_likes 
	INNER JOIN users ON tweet_likes.user_id=users.id
	{'WHERE tweet_likes.tweet_id=?' if tweet_id else ""}"""
	print(query)
	success, tweet_likes = db.get_all(query, (tweet_id,) if tweet_id else ())
	# print("tweet_likes")
	# print(tweet_likes)
	if success:
		for tweet_like in tweet_likes:
			return_data.append({ 
					"tweetId": tweet_like[0],
					"userId": tweet_like[1],
					"username": tweet_like[2]
			})
	return jsonify(return_data), 200


@app.route("/api/tweet-likes", methods=["POST"])
def tweet_likes_post():
	"""Expected Data:
	loginToken: string - jwt
	content: string
	"""
	return_data = []
	response_code = 201
	login_token = utils.decode_login_token(request.json.get('loginToken'))
	user_id = login_token.get("userId")
	tweet_id = request.json.get("tweetId")

	success, tweet = db.get_one("SELECT id FROM tweets WHERE id=?", (tweet_id,))

	if not tweet_id or not tweet:
		return jsonify({"status": "error", "message":"Invalid Tweet Id"}), 500
	if not tweet_id:
		return jsonify({"status": "error", "message":"Invalid User Id"}), 500
	
	# check if user has already liked that tweet

	success, tweet_like = db.get_one("SELECT id, user_id FROM tweet_likes WHERE tweet_id=? AND user_id=?", (tweet_id, user_id))

	if success and tweet_like:
		# User has already liked this tweet
		return jsonify({"status": "error", "message":"User has already liked this tweet"}), 500
	
	query ="""INSERT INTO tweet_likes (user_id, tweet_id) VALUES (?,?)"""
	success, tweet_id = db.insert_one(query, (user_id, tweet_id))
	
	return jsonify(None), response_code

#
# NO PATCH
#

@app.route("/api/tweet-likes", methods=["DELETE"])
def tweet_likes_delete():
	return_data = None
	response_code = 204
	login_token = utils.decode_login_token(request.json.get('loginToken'))
	user_id = login_token.get("userId")
	print(user_id)
	tweet_id = request.json.get("tweetId")

	success, tweet = db.get_one("SELECT id, content FROM tweets WHERE id=?", (tweet_id,))
	print(tweet)
	if not tweet_id or not tweet:
		return jsonify({"status": "error", "message":"Invalid Tweet Id"})

	success, tweet_like = db.get_one("SELECT id, user_id, tweet_id FROM tweet_likes WHERE tweet_id=? AND user_id=?", (tweet_id,user_id))
	print(tweet_like)
	if success and not tweet_like:
		response_code = 500
		return jsonify({"status": "error", "message":"User has not liked this tweet"})

	db.delete_one("DELETE FROM tweet_likes WHERE tweet_id=? AND user_id=?", (tweet_id,user_id))

	return jsonify(None), response_code