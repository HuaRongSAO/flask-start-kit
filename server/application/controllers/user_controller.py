from application.models import User


def get_user_by_id(id):
    """ id 查询用户"""
    user = User.query.filter_by(id=id).first()
    return user


def get_user_list(pageIndex=0, pageSize=10):
    """ 分页查询 """
    users = User.query.limit(pageSize).offset(pageIndex * pageSize)
    return users


def get_user_count():
    """ 获取用户总数 """
    users = User.query.all()
    count = len(users)
    return count


def create_user():
    user = User(username='', email='', phone='', password='').save()
    return user
