from flask import flash, redirect, render_template, url_for
from flask_login import (
	login_required,
	login_user,
	logout_user
	)
from . import Siswa

@Siswa.route('/Siswa')
@login_required
def index():
	return render_template('Siswa/index.html')

@Siswa.route('/Siswa/Tagihan')
def index():
	return render_template('Siswa/Tagihan.html')