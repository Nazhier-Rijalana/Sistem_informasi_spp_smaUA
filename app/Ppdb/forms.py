from flask_wtf import FlaskForm
from wtform importSubmitField, DecimalField, BooleanField, IntegerField, FileFieldValidationError
from wtforms.valdators import DataRequired
from ..model.Ppdb import Ppdb

class Siswa_baru():
	nama = StringField('nama_siswa', validators=[DataRequired()])
	asal_sekolah = StringField('asal_sekolah', validators=[DataRequired()])
	alamat = StringField('alamat', validators=[DataRequired()])
	nomer_hp = StringField('alamat', validators=[DataRequired()])
	kelas = DecimalField('kelas', validators=[DataRequired()])
	studi = DecimalField('studi', validators=[DataRequired()])
	no_induk = DecimalField('no_induk', validators=[DataRequired()])
	nama_ayah = StringField('nama_ayah', validators=[DataRequired()])
	nama_ibu = StringField('nama_ibu', validators=[DataRequired()])
	pekerjaan_ayah = StringField('pekerjaan_ayah', validators=[DataRequired()])
	pekerjaan_ibu = StringField('pekerjaan_ibu', validators=[DataRequired()])
	penghasilan_ayah = DecimalField('penghasilan_ayah', validators=[DataRequired()])
	penghasilan_ibu = DecimalField('penghasilan_ibu', validators=[DataRequired()])
	status_siswa = BooleanField()
	nisn = IntegerField('nisn', validators=[DataRequired()])
	foto_3x4 = FileField(u'foto_3x4', [validators.regexp(u'^[^/\\]\.png$')])
	UNAS = DecimalField('unas', validators=[DataRequired()])