import hashlib
from flask import current_app
def password_hashing_deprecate(password):
    """
    Returns sha512 from password and app.config['SECRET_KEY']
    :param password: password string
    :return: salted and hashed password
    """
    return hashlib.pbkdf2_hmac('sha512',password.encode('utf-8'),current_app.config['SECRET_KEY'].encode('utf-8'),66766).hex()#fix me 66766 is for no reason
