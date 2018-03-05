import datetime


# 返回当前时间
def now_datetime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
