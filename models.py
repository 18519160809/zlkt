# 存放数据库的表
from datetime import datetime

from sqlalchemy import ForeignKey

from exts import db
from werkzeug.security import generate_password_hash


# 创建用户的数据库模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    # question = db.relationship('Question', backref=db.backref('author'))

    # def __init__(self, *args, **kwargs):
    #     telephone = kwargs.get('telephone')
    #     username = kwargs.get('username')
    #     password = kwargs.get('password')
    #
    #     self.telephone = telephone
    #     self.username = username
    #     self.password = generate_password_hash(password)


# 创建文章的数据库模型
class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # now() 获取的是服务器第一次运行的时间
    # now 每一次创建模型时的时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.Integer, ForeignKey('user.id'))

    author = db.relationship('User', backref=db.backref('question'))


# 创建回答模型
class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())

    # 建立问题外键
    question_id = db.Column(db.Integer, ForeignKey('question.id'))
    # 建立作者外键
    author_id = db.Column(db.Integer, ForeignKey('user.id'))

    # 指定在ORM中的关系
    # 1跟问题关联起来
    question = db.relationship('Question', backref=db.backref('answer', order_by=id.desc()))
    # 2 跟作者关联起来
    author = db.relationship('User', backref=db.backref('answer'))
