from flask import current_app
import bcrypt
import jwt
import datetime



def hash_password(raw):
    return bcrypt.hashpw(raw.encode('UTF-8'), bcrypt.gensalt())


def check_password(raw, hashed):
    return bcrypt.checkpw(raw.encode('UTF-8'), hashed)


def generate_login_token(userId, username):
    return (jwt.encode({'userId': userId, "username": username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, current_app.config['SECRET_KEY'])).decode('UTF-8')


def decode_login_token(token):
    """Returns the decoded JWT as a dictionary"""
    try:
        decoded = jwt.decode(token, current_app.config["SECRET_KEY"], verify=False)
        return decoded
    except jwt.ExpiredSignatureError:
        print("Token is expired.")
        if current_app.config["DEBUG"]:
            # Bypass Expiry for development
            return decoded
        return False
    except Exception as e:
        print("JWT Error", e)