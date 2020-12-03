# Follows

## GET

---

The GET method for this endpoint requires a userId and will send back information about all users the userId follows . This endpoint will always return an array of objects.

In the example, we send an object with the userId 3. The API returns information about all users that user 3 follows. The example shows that user 3 follows user 1 and 2.


An error will be returned if the userId does not exist.


SUCCESS HTTP CODE: 200
Example Data:

JSON Params Sent:
    { 
      userId: 2
    }

JSON Data Returned: 
    [
      { 
          "userId": 1,
          "email": "test@mail.com",
          "username": "d",
          "bio": "d",
          "birthdate": "0000-00-00"
      }
    ]
    
---

## POST

---

URL:
https://your-domain.comapi/follows
The POST method for this endpoint will craete a follow relationship between two users.

Send the information about the users as an object.


In the example, we send an object with the loginToken and followId. The followId corresponds to the userId of the person we would like to follow. The loginToken represents the user doing the follow and the followId represents the user being followed.


An error will be returned if the loginToken or followId are invalid.


SUCCESS HTTP CODE: 204
Example Data:

JSON Data Sent:
    { 
      "loginToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjUsInVzZXJuYW1lIjoiNXMiLCJleHAiOjE2MDY4ODc5ODB9.Pj3BL-Aq8FPLnVz0DRNcnWf_PuJxrfmJqfc96rCfk5Y",
      "followId": "4"
    }

No data returned

---

## PATCH

---

NO PATCH


---

## DELETE

---

URL:
https://your-domain.comapi/follows
The DELETE method for this endpoint will delete a follow relationship (un-following a user).

In the example, we send an object with the loginToken and followId. The followId corresponds to the userId of the person we would like to unfollow. The loginToken represents the user doing the unfollow and the followId represents the user being un-followed. No data is returned on valid deletion.


An error will be returned if the loginToken or followId are invalid


SUCCESS HTTP CODE: 204
Example Data:

JSON Data Sent:
    { 
      "loginToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjUsInVzZXJuYW1lIjoiNXMiLCJleHAiOjE2MDY4ODc5ODB9.Pj3BL-Aq8FPLnVz0DRNcnWf_PuJxrfmJqfc96rCfk5Y",
      "followId": "2"

    }

No data returned