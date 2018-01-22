from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
import Base64

from app import db, login

class Siswa(UserMixin, db.Model):

	__tablename__='adminuser'

	@property
	def password(self):
		pass

	@password.setter
	def password(self, password):
		pass

	def verify_password(self, password):
		pass

	def __repr__(self):
		pass

@login.user_loader
def load_user(user_id):
	return Admin.query.get(int(user_id))
