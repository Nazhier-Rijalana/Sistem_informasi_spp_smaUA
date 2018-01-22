from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from app import db

class Ppdb(db.Model):

	__tablename__='pendaftaran'