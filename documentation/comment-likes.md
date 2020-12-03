# Comment Likes

## GET

---

URL:
https://your-domain.com/api/comment-likes
The GET method for this endpoint will send back either all, or specific comment likes based on comments. This endpoint will always return an array of objects.

If you want all likes, simply make the GET request and send no data. If you want likes from specific comments, send the comment Id


In the example, we send the numeric id 4. The API returns all likes on comment 4. If you want all likes on all comments, send no data.


An error will be returned if any commentId does not exist.


SUCCESS HTTP CODE: 200
Example Data:

JSON Data Sent:
    { 
      "commentId": 4 
    }

JSON Data Returned: 
    [
      { 
          "commentId": 4,
          "userId": 1,
          "username": "Samson212"
      },
      { 
          "commentId": 4,
          "userId": 1,
          "username": "Samson212"
      },
    ]
    

## POST

---

URL:
https://your-domain.com/api/comment-likes
The POST method for this endpoint will create a new like for a user on a specific comment.

Send the loginToken and commentId in an object.


In the example, we send an object loginToken and commentId. The newly created comment like is returned.


An error will be returned if the loginToken or commentId is invalid. An error will also be sent if the user has already 'liked' the comment


SUCCESS HTTP CODE: 201
Example Data:

JSON Data Sent:
    { 
      "loginToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjUsInVzZXJuYW1lIjoiNXMiLCJleHAiOjE2MDY4ODc5ODB9.Pj3BL-Aq8FPLnVz0DRNcnWf_PuJxrfmJqfc96rCfk5Y",
      "commentId": 4
    }

    { 
        "commentId": 4,
        "userId": 1,
        "username": "Samson212"
    },
      

## PATCH

---

NO PATCH

## DELETE

---

URL:
https://your-domain.com/api/comment-likes
The DELETE method for this endpoint will delete a comment like if a valid loginToken and commentId combo are sent.

In the example, we send an object with the loginToken for our user and commentId. No data is returned on a successful deletion.


An error will be returned if the loginToken and commentId combo are not valid (the user has not liked that comment or that comment does not exist).


SUCCESS HTTP CODE: 204
Example Data:

JSON Data Sent:
    { 
      "loginToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjUsInVzZXJuYW1lIjoiNXMiLCJleHAiOjE2MDY4ODc5ODB9.Pj3BL-Aq8FPLnVz0DRNcnWf_PuJxrfmJqfc96rCfk5Y",
      "commentId": "4"
    }

No JSON Returned