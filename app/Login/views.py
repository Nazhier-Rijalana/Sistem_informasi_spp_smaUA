from flask import flash, redirect, render_template, url_for
from flask_login import (
	login_required,
	login_user,
	logout_user
	)
from . import auth
from forms import LoginForm, RegistrationForm
from .. import db 
from ..models import Siswa

@auth.route('/Registrasi', methods=['GET', 'POST'])
def Registrasi():
	form = RegistrationForm()
	if form.validate_on_submit():
		siswa = Siswa(
			)
		db.session.add(Siswa)
		db.session.commit()
		flash("Data siswa Berhasil di masukkan")
		return redirect(url_for('Login.Registrasi'))
	return render_template('Login/Registrasi.html', form=form, title='Registrasi Siswa Baru' )

