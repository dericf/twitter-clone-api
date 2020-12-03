# Comments

## GET

---

URL:
https://your-domain.com/api/comments
The GET method for this endpoint will send back specific comments based on tweets. This endpoint will always return an array of objects.

If you want comments from specific tweets, send the tweet Id


In the example, we send the numeric id 2. The API returns all comments on tweets 2.


An error will be returned if any tweetId does not exist.


SUCCESS HTTP CODE: 200
Example Data:

JSON Data Sent:
    { 
      "tweetId": 2 
    }

JSON Data Returned: 
    [
      { 
          "commentId": 1,
          "tweetId": 2,
          "userId": 1,
          "username": "Samson212",
          "content": "This is a comment....",
          "createdAt": "2020-12-12"
      },
      { 
          "commentId": 2,
          "tweetId": 2,
          "userId": 1,
          "username": "Samson212",
          "content": "This is another comment...",
          "createdAt": "2020-12-13"
      },
    ]

## POST

---

URL:
https://your-domain.com/api/comments
The POST method for this endpoint will create a new comment for a user on a specific tweet.

Send the loginToken, tweetId and content in an object.


In the example, we send an object loginToken, tweetId, and content. JSON data of the comment is sent back on success.


An error will be returned if the loginToken or tweetId is invalid. Comments have a limit of 150 characters!


SUCCESS HTTP CODE: 201
Example Data:

JSON Data Sent:
    { 
      "loginToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjUsInVzZXJuYW1lIjoiNXMiLCJleHAiOjE2MDY4ODc5ODB9.Pj3BL-Aq8FPLnVz0DRNcnWf_PuJxrfmJqfc96rCfk5Y",
      "tweetId": 4,
      "content": "Adding a comment..."
    }

JSON Data Returned:
    { 
        "commentId": 5,
        "tweetId": 4,
        "userId": 3,
        "username": "DallasStone",
        "content": "Adding a comment...",
        "createdAt": "2020-07-13"
    }
      

## PATCH

---

URL:
https://your-domain.com/api/comments
The PATCH method for this endpoint will update a comment if the token and comment match (the user with the token owns the comment).

Send the information about the user and comment as an object.


In the example, we send an object with the loginToken, commentId and content. We are sent back conformation information about our updated tweet.


An error will be returned if you try to change the comment to be too long or the login token does not own the comment being edited.


SUCCESS HTTP CODE: 200
Example Data:

JSON Data Sent:
    { 
      "loginToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjUsInVzZXJuYW1lIjoiNXMiLCJleHAiOjE2MDY4ODc5ODB9.Pj3BL-Aq8FPLnVz0DRNcnWf_PuJxrfmJqfc96rCfk5Y",
      "commentId": 5,
      "content": "Updating a comment..."
    }

JSON Data Returned: 
      { 
        "commentId": 5,
        "tweetId": 4,
        "userId": 3,
        "username": "DallasStone",
        "content": "Updating a comment...",
        "createdAt": "2020-07-13"
    }
    

## DELETE

---

URL:
https://your-domain.com/api/comments
The DELETE method for this endpoint will delete a comment if a valid loginToken and commentId combo are sent.

In the example, we send an object with the loginToken for our user and commentId. No data is sent back on a valid delete


An error will be returned if the loginToken and comment combo are not valid (the user does not own that comment or that comment does not exist).


SUCCESS HTTP CODE: 204
Example Data:

JSON Data Sent:
    { 
      "loginToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjUsInVzZXJuYW1lIjoiNXMiLCJleHAiOjE2MDY4ODc5ODB9.Pj3BL-Aq8FPLnVz0DRNcnWf_PuJxrfmJqfc96rCfk5Y",
      "commentId": "1"
    }

No JSON Returned