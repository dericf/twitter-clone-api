# Users

## GET

---

URL:
https://your-domain.com/api/users
The GET method for this endpoint will send back either all, or specific user information. This endpoint will always return an array of objects.

If you want all users, simply make the GET request and send no data. If you want specific user information, send the user Id of the user


In the example, we send the userId of 1. The API returns information about user 1. If you want all users that are signed up, send no data.

The data sent back will always be an array.


An error will be returned if a userId does not exist.


SUCCESS HTTP CODE: 200
Example Data:

JSON Params Sent:
    { 
      userId: 1 
    }

JSON Data Returned: 
    [
      { 
          "userId": 1,
          "email": "john@email.com",
          "username": "johnD",
          "bio": "john's bio...",
          "birthdate": "1980-01-01"
      }
    ]
    

## POST

---

URL:
https://your-domain.com/api/users
The POST method for this endpoint will create a new user if there is no conflicting user.

Send the information about the user as an object.


In the example, we send an object with the email, username, password, bio and birthdate of our new user. We are sent back conformation information about our new user. We are also sent back a loginToken!


An error will be returned if a username or email already exists.


SUCCESS HTTP CODE: 201
Example Data:

JSON Data Sent:
    { 
      "email": "DallasStone@email.com",
      "username": "DallasStone",
      "password": "IStoleChristmas",
      "bio": "Dallas's Bio...",
      "birthdate": "1980-02-01"
    }

JSON Data Returned: 
    { 
        "userId": 23,
        "email": "DallasStone@email.com",
        "username": "DallasStone",
        "bio": "Dallas's Bio...",
        "birthdate": "1980-02-01",
        "loginToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjUsInVzZXJuYW1lIjoiNXMiLCJleHAiOjE2MDY4ODc5ODB9.Pj3BL-Aq8FPLnVz0DRNcnWf_PuJxrfmJqfc96rCfk5Y"
    }
    

## PATCH

---

URL:
https://your-domain.com/api/users
The PATCH method for this endpoint will update a user if there is no conflicting information in the change.

Send the information about the user as an object. The loginToken is required!


In the example, we send an object with the loginToken and updated bio of our user. We are sent back conformation information about our updated user.


An error will be returned if you try to change the username or email to one that already exists or if you send invalid data.


SUCCESS HTTP CODE: 200
Example Data:

JSON Data Sent:
    { 
      "loginToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjUsInVzZXJuYW1lIjoiNXMiLCJleHAiOjE2MDY4ODc5ODB9.Pj3BL-Aq8FPLnVz0DRNcnWf_PuJxrfmJqfc96rCfk5Y",
      "bio": "Everyone is finally together for christmas!"
    }

JSON Data Returned: 
    { 
        "userId": 23,
        "email": "DallasStone@email.com",
        "username": "DallasStone",
        "bio": "Everyone is finally together for christmas!",
        "birthdate": "1980-02-01",
    }
    


## DELETE

---

URL:
https://your-domain.com/api/users
The DELETE method for this endpoint will delete a user if a valid loginToken and password are sent.

In the example, we send an object with the loginToken and password for our user. No data is returned on a valid delete.


An error will be returned if the loginToken and password combo are not valid.


SUCCESS HTTP CODE: 204
Example Data:

JSON Data Sent:
    { 
      "loginToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjUsInVzZXJuYW1lIjoiNXMiLCJleHAiOjE2MDY4ODc5ODB9.Pj3BL-Aq8FPLnVz0DRNcnWf_PuJxrfmJqfc96rCfk5Y",
      "password": "123456"

    }

No Data Returned