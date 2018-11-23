import os

from flask import Blueprint, jsonify, render_template, request, session

from user.models import User, db, Facility, House, HouseImage
from utils.functions import is_login

house_blueprint = Blueprint('house', __name__)


@house_blueprint.route('/house/', methods=['GET'])
@is_login
def house():
    return render_template('myhouse.html')


@house_blueprint.route('/n_house/', methods=['GET'])
@is_login
def n_house():
    return render_template('newhouse.html')


@house_blueprint.route('/new_house/', methods=['POST', 'GET'])
@is_login
def new_house():
    user_id = session['user_id']
    # user = User.query.get(user_id)
    housess = House()
    house_m = request.form
    housess.user_id = user_id
    housess.title = house_m.get('title')
    housess.price = house_m.get('price')
    housess.area_id = house_m.get('area_id')
    housess.address = house_m.get('address')
    housess.room_count = house_m.get('room_count')
    housess.acreage = house_m.get('acreage')
    housess.unit = house_m.get('unit')
    housess.capacity = house_m.get('capacity')
    housess.beds = house_m.get('beds')
    housess.deposit = house_m.get('deposit')
    housess.min_days = house_m.get('min_days')
    housess.max_days = house_m.get('max_days')
#     房屋和设施是多对多关系
    facilities = house_m.getlist('facility')

    for facility in facilities:
        facility1 = Facility.query.filter_by(id=facility).first()
        housess.facilities.append(facility1)
    db.session.add(housess)
    db.session.commit()
    housesss_id = housess.id
    session['housesss_id'] = housesss_id
    return jsonify(code=200, housesss_id=housesss_id)


@house_blueprint.route('/new_picture/', methods=['POST', 'GET'])
@is_login
def new_picture():
    house_image = request.files.get('house_image')
    MEDIA_ROOT = os.path.join('static', 'images')
    path = os.path.join(MEDIA_ROOT, house_image.filename)
    house_image.save(path)
    user_id = session['user_id']
    housesss_id = session['housesss_id']
    # 房屋与图片配置是一对多关系
    # 保存到数据库
    # houseImage = HouseImage()
    # house2 = House()
    house1 = House.query.filter_by(user_id=user_id).filter_by(id=housesss_id).first()
    # house2 = House.query.filter_by(id=housesss_id).first()
    # house2 = request.
    house1.index_image_url = path
    db.session.add(house1)
    db.session.commit()
    return jsonify(code=200)


# 获取已经上传房源的信息
@house_blueprint.route('/new_user_picture/', methods=['POST', 'GET'])
@is_login
def new_user_picture():
    user_id = session['user_id']
    # house_image = HouseImage()
    new_house = House.query.filter_by(user_id=user_id).all()



    # house1 = house_new.query.filter_by(user_id=user_id).first()
    list2=[]
    for i in new_house:
        list2.append(i.to_dict())
    return jsonify(code=200, to_dict=list2)


    # # 获取房屋ID
    # house_id = house1.id
    # # 获取房屋标题
    # house_title = house1.title
    # # 获取城区
    # house_user_id = house1.area_id
    # # 获取价格
    # house_price = house1.price
    # # 获取发布时间
@house_blueprint.route('/detail/<int:id>/', methods=['POST', 'GET'])
@is_login
def detail(id):
    return render_template('detail.html')
# 订单