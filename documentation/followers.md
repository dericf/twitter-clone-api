
# Followers

## GET

---

URL:
https://your-domain.com/api/followers
The GET method for this endpoint requires a userId and will send back information about all users the follow that user. This endpoint will always return an array of objects.

In the example, we send an object with the userId 3. The API returns information about all users that follow user 3. The example shows that user 3 is followed by user 1 and 2.


An error will be returned if the userId does not exist.


SUCCESS HTTP CODE: 200
Example Data:

JSON Params Sent:
```
    { 
      userId: 3 
    }
```

JSON Data Returned: 
```
    [
      { 
          "userId": 1,
          "email": "samson@email.com",
          "username": "Samson212",
          "bio": "Samson's bio...",
          "birthdate": "1971-06-23"
      },
      { 
          "userId": 2,
          "email": "john@email.com",
          "username": "johnD",
          "bio": "john's bio...",
          "birthdate": "1980-01-01"
      },
    ]
```

---

## POST

---

NO POST

---

## PATCH

---

NO PATCH

---

## DELETE

---

NO DELETE