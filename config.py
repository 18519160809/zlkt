# 项目中的所有设置都放在config文件中

import os

# 开启调试模式
DEBUG = True


# 使用session 的时候需要添加这一项设置
SECRET_KEY = os.urandom(24)


# 数据库的相关配置
# SQLALCHEMY_DATABASE_URI = dialect + driver://username:password@host:port/database
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'zlkt'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME,PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False

# 设置每次请求结束后会自动提交数据库中的改动
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

# 使用flask——wtf 需要设置防止csrf
SECRET_KEY = 'hello'
