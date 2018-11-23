import random

# from flask_session import Session
from functools import wraps

from flask import session,jsonify,redirect,url_for
from flask_wtf import CsrfProtect

from user.models import db


def init_ext(app):
    # Session(app)
    CsrfProtect(app)
    db.init_app(app)


def get_mysql_database(database):
    return '{}+{}://{}:{}@{}:{}/{}'.format(
                                           database['DIALECT'],
                                           database['DRIVER'],
                                           database['USER'],
                                           database['PASSWORD'],
                                           database['HOST'],
                                           database['PORT'],
                                           database['DB']
                                           )


def tp_random():
    a = 'sdajfhapiweuasddsabjk;bfgpiuwfghkaj;sg'
    b = ''
    for i in range(4):
        b += random.choice(a)
    return b


def is_login(func):
    @wraps(func)
    def check(*args, **kwargs):
        try:
            user_id = session['user_id']
        except Exception as e:
            # return jsonify({'code': 500})
            return redirect(url_for('user.login'))
        return func(*args, **kwargs)
    return check
