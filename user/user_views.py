
import os
import re

from flask import Blueprint, render_template, jsonify, request, redirect, url_for, session

from werkzeug.security import generate_password_hash, check_password_hash

from user.forms import RegisterForm, LoginForm
from user.models import User, db
from utils.functions import tp_random, is_login

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/rad/', methods=['GET', 'POST'])
def rad():
    picture1 = tp_random()
    return jsonify({'code': 200, 'picture1': picture1})


@user_blueprint.route('/register/', methods=['GET'])
def register():
    picture = tp_random()
    return render_template('register.html', picture=picture)
# ajax回调函数的时候是数据


@user_blueprint.route('/my_register/', methods=['POST'])
def my_register():
    # 获取注册提交过来的信息

    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        user.name = form.mobile.data
        user.pwd_hash = generate_password_hash(form.passwd.data)
        db.session.add(user)
        db.session.commit()
        return jsonify({'code': 200, 'msg': '注册成功'})

    else:
        return jsonify({'code': 1000})


@user_blueprint.route('/create/')
def create():
    db.create_all()
    return '创建数据库成功'


@user_blueprint.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')


@user_blueprint.route('/my_login/', methods=['POST'])
def my_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.mobile.data).first()
        if check_password_hash(user.pwd_hash, form.passwd.data):
            session['user_id'] = user.id
            return jsonify({'code': 200, 'msg': '登录成功'})
    else:
        return jsonify({'code': 500})


@user_blueprint.route('/index/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@user_blueprint.route('/my/', methods=['GET', 'POST'])
@is_login
def my():
    return render_template('my.html')


@user_blueprint.route('/my_info/', methods=['GET', 'POST'])
@is_login
def my_info():
    user_id = session['user_id']
    user = User.query.get(user_id)
    user_info = user.to_basic_dict()
    return jsonify(user_info=user_info, code=200)


@user_blueprint.route('/user_profile/', methods=['GET', 'POST'])
@is_login
def user_profile():
    return render_template('profile.html')


# 图片
@user_blueprint.route('/profile/', methods=['POST', 'PATCH', 'GET'])
@is_login
def profile():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(os.path.join(BASE_DIR, 'static'), 'media')

    upload_img = request.files.get('avatar')
    # 将图片保存到本地

    path = os.path.join(MEDIA_ROOT, upload_img.filename)
    upload_img.save(path)
    # 在将图片文件保存到数据库

    user_id = session['user_id']
    user = User.query.get(user_id)
    avatar = upload_img.filename
    user.avatar = avatar
    db.session.add(user)
    db.session.commit()
    user_info = user.to_basic_dict()
    return jsonify(code=200, user_info=user_info)


# 用户名
@user_blueprint.route('/user_name/', methods=['PATCH'])
@is_login
def user_name():
        username = request.form.get('username')
        #     获取用户
        user_id = session['user_id']
        user = User.query.get(user_id)
    #    更新字段
        user.phone = username
        db.session.add(user)
        db.session.commit()
        return jsonify(code=200)


# 实名认证
@user_blueprint.route('/auth/', methods=['PATCH','POST','GET'])
@is_login
def auth():
    return render_template('auth.html')


@user_blueprint.route('/user_auth/', methods=['PATCH', 'POST', 'GET'])
@is_login
def user_auth():
    user_id = session['user_id']
    user = User.query.get(user_id)
    # id_name = user.id_name
    # id_card = user.id_card
    # if all([id_name, id_card]):
    #     return jsonify(code=200, id_card=id_card, id_name=id_name)
    # else:
    id_name1 = request.form.get('real_name')
    id_card1 = request.form.get('id_card')
    if all([id_name1, id_card1]):
        #     验证是否完全匹配
        if re.match(r'^[1-9]\d{16}[0-9X]$', id_card1):
            user.id_name = id_name1
            user.id_card = id_card1
            user.add_update()
            return jsonify(code=200, d_card=id_card1, id_name=id_name1)
        else:
            return jsonify(code=500, msg='填写有误')
    if not id_name1:
        return jsonify(code=500, msg='请填写真实姓名')
    if not id_card1:
        return jsonify(code=500, msg='请填写身份证号码')


# 验证是否是否实名
@user_blueprint.route('/user_user_auth/', methods=['PATCH', 'POST', 'GET'])
@is_login
def user_user_auth():
    user_id = session['user_id']
    user = User.query.get(user_id)
    id_name = user.id_name
    id_card = user.id_card
    if all([id_name, id_card]):
        return jsonify(code=200)
    else:
        return jsonify(code=400)


# @user_blueprint.route('/upload/', methods=['GET'])
# def ui_img():
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     MEDIA_ROOT = 'F:/'


# @user_blueprint.before_request
# def before_request():
#     list = ['/user/login/', '/user/register/']
#     path = request.path
#     try:
#         user_id = session['user_id']
#         if user_id:
#             return None
#         if path in list:
#             return None
#     except Exception as e:
#         return jsonify({'code': 500})
