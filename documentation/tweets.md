# Tweets

## GET

---

URL:
https://your-domain.com/api/tweets
The GET method for this endpoint will send back either all, or specific tweets based on user. This endpoint will always return an array of objects.

If you want all tweets, simply make the GET request and send no data. If you want tweets from specific users, send the user Id


In the example, we send the numeric id 1. The API returns tweets by user 1. If you want all tweets, send no data.


An error will be returned if any userId does not exist.


SUCCESS HTTP CODE: 200
Example Data:

JSON Params Sent:
    { 
      userId: 1 
    }

JSON Data Returned: 
    [
      { 
          "tweetId": 1,
          "userId": 1,
          "username": "Samson212",
          "content": "This is a tweet content",
          "createdAt": "2020-12-01"
      },
      { 
          "tweetId": 2,
          "userId": 1,
          "username": "Samson212",
          "content": "Another tweet",
          "createdAt": "2020-12-02"
      },
    ]

---
## POST
---
URL:
https://your-domain.com/api/tweets
The POST method for this endpoint will create a new tweet for a user.

Send the loginToken and content in an object.


In the example, we send an object with loginToken and content. An object is sent back on success.


An error will be returned if the loginToken is invalid. The tweet has a character limit of 200


SUCCESS HTTP CODE: 201
Example Data:

JSON Data Sent:
    { 
      "loginToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjUsInVzZXJuYW1lIjoiNXMiLCJleHAiOjE2MDY4ODc5ODB9.Pj3BL-Aq8FPLnVz0DRNcnWf_PuJxrfmJqfc96rCfk5Y",
      "content": "A tweet..."
    }

JSON Data Returned
    {
      "tweetId": 5,
      "userId": 3,
      "username": "DallasStone",
      "content": "A tweet...",
      "createdAt": "2020-04-15"
    }
      


---

## PATCH

---

URL:
https://your-domain.com/api/tweets
The PATCH method for this endpoint will update a tweet if the token and tweet match (the user with the token owns the tweet).

Send the information about the user and tweet as an object.


In the example, we send an object with the loginToken, tweetId and update content. We are sent back conformation information about our updated tweet.


An error will be returned if you try to change the tweet to be too long or the login token does not own the tweet being edited.


SUCCESS HTTP CODE: 200
Example Data:

JSON Data Sent:
    { 
      "loginToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjUsInVzZXJuYW1lIjoiNXMiLCJleHAiOjE2MDY4ODc5ODB9.Pj3BL-Aq8FPLnVz0DRNcnWf_PuJxrfmJqfc96rCfk5Y",
      "tweetId": 2,
      "content": "EDITING A TWEET"
    }

JSON Data Returned: 
    { 
      "tweetId": 2,
      "content": "EDITING A TWEET"
    }
    


---

## DELETE

---

URL:
https://your-domain.com/api/tweets
The DELETE method for this endpoint will delete a tweet if a valid loginToken and tweetId combo are sent.

In the example, we send an object with the loginToken for our user and tweetId. No data is sent back on valid delete.


An error will be returned if the loginToken and tweetId combo are not valid (the user does not own that tweet or that tweet does not exist).


SUCCESS HTTP CODE: 204
Example Data:

JSON Data Sent:
    { 
      "loginToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjUsInVzZXJuYW1lIjoiNXMiLCJleHAiOjE2MDY4ODc5ODB9.Pj3BL-Aq8FPLnVz0DRNcnWf_PuJxrfmJqfc96rCfk5Y",
      "tweetId": "2"

    }

No data returned