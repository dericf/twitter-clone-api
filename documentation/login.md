# Login

## GET

---

NO GET

## POST

---

URL:
https://your-domain.com/api/login
The POST method for this endpoint will log a user in if the username / password combo are correct.

Send the information about the user as an object.


In the example, we send an object with the email and password of our user. We are sent back conformation information about our new user. We are also sent back a loginToken!
Note you can send either the email or the username for your user.


An error will be returned if the login information is invalid.


SUCCESS HTTP CODE: 201
Example Data:

JSON Data Sent:
    { 
      "email": "DallasStone@email.com",
      "password": "IStoleChristmas"
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

NO PATCH

## DELETE

---

URL:
https://your-domain.com/api/login
The DELETE method for this endpoint will destroy the loginToken provided.

In the example, we send an object with the loginToken for our user. No data is sent back on a valid delete.


An error will be returned if the loginToken is invalid


SUCCESS HTTP CODE: 204
Example Data:

JSON Data Sent:
```
    { 
      "loginToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjUsInVzZXJuYW1lIjoiNXMiLCJleHAiOjE2MDY4ODc5ODB9.Pj3BL-Aq8FPLnVz0DRNcnWf_PuJxrfmJqfc96rCfk5Y"
    }
```

No Data Returned