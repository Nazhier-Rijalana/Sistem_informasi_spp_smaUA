from flask_wtf import FlaskForm
from wtform import PasswordField, StringField, SubmitField, ValidationError
from wtforms.valdators import DataRequired, Email, EqualTo
from ..model.Siswa_models, import Siswa
from ..model.Admin_models import Admin

class LoginForm(FlaskForm):
	Username = StringField('Username', validators=[DataRequired()])
	Password = PasswordField('Password', validators=[DataRequired()])
	Submit = SubmitField('Login')