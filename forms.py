from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField, TextAreaField
from wtforms.validators import length, EqualTo, DataRequired


class RegistForm(FlaskForm):
    telephone = StringField(
        render_kw={'class': "form-control", 'id': "exampleInputEmail1", 'placeholder': "手机号码"},
        validators=[length(11)]

    )
    username = StringField(
        render_kw={'class': "form-control", 'id': "exampleInputName", 'placeholder': "用户名"},
        validators=[DataRequired()]
    )
    password1 = PasswordField(
        render_kw={'class': "form-control", 'id': "exampleInputPassword1", 'placeholder': "密码"},
        validators=[DataRequired()]
    )
    password2 = PasswordField(
        render_kw={'class': "form-control", 'id': "exampleInputPassword2", 'placeholder': "确认密码"},
        validators=[DataRequired(), EqualTo('password1')]
    )
    confirm = SubmitField(
        render_kw={'class': 'btn btn-primary'},
        label='立即注册'
    )


class LoginFrom(FlaskForm):
    telephone = StringField(
        render_kw={'class': "form-control", 'id': "exampleInputEmail1", 'placeholder': "手机号码"},
        validators=[length(11)]
    )

    password = PasswordField(
        render_kw={'class': "form-control", 'id': "exampleInputPassword1", 'placeholder': "密码"},
        validators=[DataRequired()]
    )

    confirm = SubmitField(
        render_kw={'class': 'btn btn-primary'},
        label='立即登录'
    )


class QuestionForm(FlaskForm):
    title = StringField(
        render_kw={'placeholder': '请输入标题', 'class': 'form-control'},
        validators=[DataRequired()],
    )

    content = TextAreaField(
        render_kw={'row': '10', 'class': 'form-control'},
        validators=[DataRequired()],
    )
    confirm = SubmitField(
        render_kw={'class': 'btn btn-primary'},
        label='立即发布'
    )



















