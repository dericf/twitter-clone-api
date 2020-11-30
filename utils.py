from flask import current_app
import bcrypt
import jwt
import datetime



def hash_password(raw):
    return bcrypt.hashpw(raw.encode('UTF-8'), bcrypt.gensalt())


def check_password(raw, hashed):
    return bcrypt.checkpw(raw.encode('UTF-8'), hashed)


def generate_login_token(userId):
    return (jwt.encode({'userId': userId, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, current_app.config['SECRET_KEY'])).decode('UTF-8')


def decode_login_token(token):
    try:
        decoded = jwt.decode(token, current_app.config["SECRET_KEY"])
        return decoded
    except jwt.ExpiredSignatureError:
        print("Token is expired.")
        return False
