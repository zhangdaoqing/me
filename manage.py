import redis

from flask import Flask
from flask_script import Manager
from flask_session import Session

from user.house_views import house_blueprint
from user.order_views import blue_orders
from user.user_views import user_blueprint
from utils.config import Config
from utils.functions import init_ext

app = Flask(__name__)
manage = Manager(app)
app.secret_key = 'aslkgfdpqiefaskhpqwe;as'

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)
Session(app)

app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')
app.register_blueprint(blueprint=blue_orders, url_prefix='/orders')
app.register_blueprint(blueprint=house_blueprint, url_prefix='/house')


app.config.from_object(Config)
init_ext(app)

if __name__ == '__main__':
    manage.run()