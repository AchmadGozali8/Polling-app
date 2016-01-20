from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

	__tablename__ = "user_login"

	#fields
	id = db.Column(db.Integer,primary_key=True)
	nama_lengkap = db.Column(db.String(120))
	email = db.Column(db.String(120), unique=True)

	def __init__(self, nama_lengkap,email):
		self.nama_lengkap = nama_lengkap
		self.email = email
	def __repr__(self):
		return "<User {}".format(self.nama_lengkap)
