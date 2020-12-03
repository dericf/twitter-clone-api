# TWEET LIKES

## GET

---

URL:
https://your-domain.com/api/tweet-likes
The GET method for this endpoint will send back either all, or specific likes based on tweet. This endpoint will always return an array of objects.

If you want all likes, simply make the GET request and send no data. If you want likes from a specific tweet, send the tweet Id


In the example, we send the numeric id 1. The API returns all likes on tweets 1. If you want all likes on all tweets, send no data.


An error will be returned if any tweetId does not exist.


SUCCESS HTTP CODE: 200
Example Data:

JSON Params Sent:
    { 
      "tweetId": 1 
    }

JSON Data Returned: 
    [
      { 
          "tweetId": 1,
          "userId": 1,
          "username": "Samson212"
      },
      { 
          "tweetId": 1,
          "userId": 2,
          "username": "johnD"
      },
    ]
    

---

## POST

---
URL:
https://your-domain.com/api/tweet-likes
The POST method for this endpoint will create a new like for a user on a specific tweet.

Send the loginToken and tweetId in an object.


In the example, we send an object loginToken and tweetId. No data is sent back on success.


An error will be returned if the loginToken or tweetId is invalid. An error will also be sent if the user has already 'liked' the tweet


SUCCESS HTTP CODE: 201
Example Data:

JSON Data Sent:
    { 
      "loginToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjUsInVzZXJuYW1lIjoiNXMiLCJleHAiOjE2MDY4ODc5ODB9.Pj3BL-Aq8FPLnVz0DRNcnWf_PuJxrfmJqfc96rCfk5Y",
      "tweetId": 4
    }

No Data Returned

---

## DELETE

---

URL:
https://your-domain.com/api/tweet-likes
The DELETE method for this endpoint will delete a like if a valid loginToken and tweetId combo are sent.

In the example, we send an object with the loginToken for our user and tweetId. No data is returned on a valid delete.


An error will be returned if the loginToken and tweetId combo are not valid (the user has not liked that tweet or that tweet does not exist).


SUCCESS HTTP CODE: 204
Example Data:

JSON Data Sent:
    { 
      "loginToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjUsInVzZXJuYW1lIjoiNXMiLCJleHAiOjE2MDY4ODc5ODB9.Pj3BL-Aq8FPLnVz0DRNcnWf_PuJxrfmJqfc96rCfk5Y",
      "tweetId": "2"
    }

No JSON Returned