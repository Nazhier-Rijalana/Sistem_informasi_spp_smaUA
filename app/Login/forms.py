from flask_wtf import FlaskForm
from wtform import PasswordField, StringField, SubmitField, ValidationError
from wtforms.valdators import DataRequired, Email, EqualTo
from ..model import Siswa

class DaftarRegistrasi(FlaskForm):
	
	def validate_NISN(self, field):
		pass

class LoginForm(FlaskForm):
	pass
