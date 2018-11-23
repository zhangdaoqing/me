from flask_wtf import FlaskForm

from wtforms import SubmitField,StringField,ValidationError

from wtforms.validators import DataRequired, EqualTo

from user.models import User


class RegisterForm(FlaskForm):
    # 注册表单验证
    # validators=[DataRequired]验证器，确保字段有值

    mobile = StringField('电话号码', validators=[DataRequired()])
    phoneCode = StringField('短信验证码', validators=[DataRequired()])
    passwd = StringField('密码', validators=[DataRequired()])
    passwd2 = StringField('确认密码', validators=[DataRequired(),
                                                EqualTo('passwd', '两次密码不一致')])

    def validate_mobile(self, field):
        user = User.query.filter_by(phone=field.data).first()
        if user:
            raise ValidationError('该用户已经注册过')
        if len(field.data) != 11:
            raise ValidationError('手机号码不正确')


class LoginForm(FlaskForm):
    mobile = StringField('电话号码', validators=[DataRequired()])
    passwd = StringField('密码', validators=[DataRequired()])

    def validate_mobile(self, field):
        user = User.query.filter_by(name=field.data).first()
        if not user:
            raise ValidationError('该用户还未注册')
