from flask import flash, redirect, render_template, url_for
from flask_login import (
	login_required,
	login_user,
	logout_user
	)
from . import Login
from forms import LoginForm, RegistrationForm
from .. import db 
from ..models import Siswa
@Login.route('/Login', methods=['GET', 'POST'])
def Login():
	form = LoginForm():
	if form.validate_on_submit():
		if is.admin():
			flash("Login Berhasil")
			return render_template('Admin/index.html')
		else:
			return render_template('Siswa/index.html')

	return render_template('Login/Login.html')