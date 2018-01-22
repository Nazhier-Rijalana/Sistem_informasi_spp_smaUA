from flask import render_template
from flask_login import login_required

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/v1/dashboard/Admin')
@login_required
def index():
	return render_template('HomePage/indexDashBoard.html', title="Dashboard Admin")

@app.route('/v1/dashboard/Siswa')
@login_required
def index():
	return render_template('HomePage/indexSiswa.html', title="Dashboard Siswa")