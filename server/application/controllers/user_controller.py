from application.models import User
from application.util import hash_encrypt, now_datetime
from sqlalchemy import or_


def get_user_by_id(id):
    """ id 查询用户"""
    user = User.query.filter_by(id=id).first_or_404()
    return user


def get_user_by_id_or_name(id):
    """ id username 查询用户 """
    user = User.query.filter(or_(User.id.like(id), User.username.like(id))).first_or_404()
    return user


def get_user_list(page_index=0, page_size=10):
    """ 分页查询 """
    users = User.query.order_by(User.id).limit(page_size).offset(page_index * page_size)
    return users


def get_user_count():
    """ 获取用户总数 """
    users = User.query.all()
    count = len(users)
    return count


def create_user(username='', email='', phone='', password=''):
    """ 创建新用户 """
    user = User(username=username, email=email, phone=phone, password=hash_encrypt(password),
                create_time=now_datetime(), update_time=now_datetime()).save()
    return user


def update_user(id='', username='', email='', phone='', password=''):
    """ 更新用户 """
    update = {}
    if username:
        update.username = username
    if password:
        update.password = hash_encrypt(password)
    if email != '':
        update.email = email
    if phone != '':
        update.phone = phone
    user = User.query.filter_by(id=id).first_or_404().update(update)
    return user


def delete_user_by_id(id):
    """ 删除用户 """
    user = User.query.filter_by(id=id).first_or_404()
    user.delete()
    return user


def delete_user_by_id_and_name(id):
    """ username 或者id 删除用户 """
    user = User.query.filter(or_(User.id.like(id), User.username.like(id))).first_or_404()
    user.delete()
    return user
