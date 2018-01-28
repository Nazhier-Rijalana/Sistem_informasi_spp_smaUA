from flask import flash, redirect, render_template, url_for
from flask_login import (
	login_required,
	login_user,
	logout_user
	)

from . import Admin

@Admin.route('/Dashboard')
@login_required
def index():
	return render_template('/Dashboard/index.html')

@Admin.route('/Dashboard/MasterPembayaran')
@login_required
def index():
	return render_template('/Dashboard/MasterPembayaran.html')

@Admin.route('Dashboard/TambahTagihan')
@login_required
def index():
	return render_template('/Dashboard/TambahTagihan.html')

@Admin.route('Dashboard/EditTagihan')
@login_required
def index():
	return render_template('/Dashboard/EditTagihan.html')

@Admin.route('Dashboard/DeleteTagihan')
@login_required
def index():
	return render_template('/Dashboard/DeleteTagihan.html')

@Admin.route('Dashboard/ListLunas')
@login_required
def index():
	return render_template('/Dashboard/ListLunas.html')

@Admin.route('Dashboard/TambahLunas/<id>')
@login_required
def index():
	return render_template('/Dashboard/TambahLunas.html')