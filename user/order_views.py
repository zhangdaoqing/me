from flask import Blueprint, render_template

from utils.functions import is_login

blue_orders = Blueprint('orders', __name__)


# @blue_orders.route('/orders/', methods=['GET', 'POST'])
# @is_login
# def orders():
#     return render_template('orders.html')