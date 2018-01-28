from flask_wtf import FlaskForm
from wtform import PasswordField, StringField, SubmitField, ValidationError
from wtforms.valdators import DataRequired, Email, EqualTo
from ..model.Siswa_models import Siswa
from ..model.Spp_models import *