from flask import flash, redirect, render_template, url_for
from flask_login import (
	login_required,
	login_user,
	logout_user
	)
from . import Ppdb

@Ppdb.route('/Ppdb')
@login_required
def index():
	return render_template('Ppdb/ListSiswa.html')

@Ppdb.route('/Ppdb/TambahSiswa')
@login_required
def TambahSiswa():
	return render_template('Ppdb/TambahSiswa.html')

@Ppdb.route('/Ppdb/UpdateSiswa/<id>')
@login_required
def EditSiswa():
	return render_template('Ppdb/UpdateSiswa.html')

@Ppdb.route('/Ppdb/DeleteSiswa/<id>')
@login_required
def DeleteSiswa():
	return render_template('Ppdb/DeleteSiswa.html')
