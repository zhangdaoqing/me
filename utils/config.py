import redis
from utils.functions import get_mysql_database
from utils.settings import DATABASES


class Config():

    SQLALCHEMY_DATABASE_URI = get_mysql_database(DATABASES)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SESSION_TYPE = redis
    # SESSION_REDIS = redis.Redis(host='127.0.0.1', port=6379)