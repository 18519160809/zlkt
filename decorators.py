from functools import wraps
from flask import url_for, session
from werkzeug.utils import redirect

# 问答页面的登录校验
# 使用装饰器来实现
# 为了让func保持原来的name 也就是让被装饰的函数名保持不变


def is_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrapper