from sqlalchemy import or_

from flask import Flask, render_template, request, redirect, url_for, session, g
from werkzeug.security import generate_password_hash

import config
from decorators import is_login
from exts import db
from models import User, Question, Answer

app = Flask(__name__)

# 导入配置文件
app.config.from_object(config)

# 初始化app
db.init_app(app)

# 导入表单类
from forms import RegistForm, LoginFrom, QuestionForm


@app.route('/')
def index():
    context = {
        'questions': Question.query.order_by('-create_time').all()
    }
    return render_template('index.html', **context)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginFrom()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(telephone=form.telephone.data).first()
        if form.password.data == user.password:
            # 存在session中 保持状态
            session['user_id'] = user.id
            return redirect(url_for('index'))
        else:
            return '用户名或密码错误！'

    return render_template('login.html', form=form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    # 实例化表单类
    form = RegistForm()
    if request.method == 'POST' and form.validate_on_submit():
        t_count = User.query.filter_by(telephone=form.data['telephone']).count()
        if t_count == 0:
            pwd = form.password1.data
            pwd1 = generate_password_hash(pwd)
            user = User(telephone=form.telephone.data, username=form.data['username'], password=pwd1)
            db.session.add(user)
            db.session.commit()
            print('chenggong')
            # 注册成功后跳转到登录页面
            return redirect(url_for('login'))
        else:
            return '该手机号已经被注册'

    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    # 注销就是退出登录，删除session就可以
    # 1 session.pop('user_id')
    # 2 del session['user_id']
    # 3 session.clear()
    session.pop('user_id')
    return redirect(url_for('login'))


@app.route('/question', methods=['GET', 'POST'])
@is_login
def question():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        que = Question(title=form.title.data, content=form.content.data, author=g.user)
        db.session.add(que)
        db.session.commit()
        # print('chenggong')
        # 注册成功后跳转到首页
        return redirect(url_for('index'))
    # else:
    #     return '该文章名已经被使用'

    return render_template('question.html', form=form)


@app.route('/detail/<question_id>')
def detail(question_id):
    q = Question.query.filter(Question.id == question_id).first()
    for i in q.answer:
        print(i.content)
    return render_template('detail.html', q=q)


@app.route('/add_answer', methods=['POST'])
@is_login
def add_answer():
    content = request.form.get('ans')
    answer = Answer(content=content)
    # user_id = session['user_id']
    # user = User.query.filter(User.id == user_id).first()
    answer.author = g.user
    question_id = request.form.get('question_id')
    qu = Question.query.filter(Question == question_id).first()
    answer.question = qu
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('detail', question_id=question_id))


@app.route('/search/')
def search():
    # 从html中得到q的内容
    q = request.args.get('q')

    # 在标题中存在q或者内容中存在都算找到
    # 用到or_  需要导入  contains 包含
    questions = Question.query.filter(or_(Question.title.contains(q), Question.content.contains(q))).order_by(
        '-create_time')

    # 如果是标题中也有q 内容中也有q 这样写 表示并且关系
    # questions = Question.query.filter(Question.title.contains(q), Question.content.contains(q)).order_by(
    #     '-create_time')

    return render_template('index.html', questions=questions)


# 钩子函数类似于django中的中间件
# 使用g对象来优从seesion中取数据判断是否登录过的代码
# 这是before_reqeust 钩子函数
@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            g.user = user


# 这是上下文处理器的勾子函数
@app.context_processor
def my_context_processor():
    if hasattr(g, 'user'):
            return {'user': g.user}
    else:
        return {}


if __name__ == '__main__':
    app.run()
