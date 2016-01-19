from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):

	__tablename__ = "user_login"

	#fields
	id = db.Column(db.Integer,primary_key=True)
	full_name=db.Column(db.String(120))
	email = db.Column(db.String(120), unique=True)

	def __init__(self, full_name,email):
		self.full_name = full_name
		self.email = email
	def __repr__(self):
		return "<User {}".format(self.full_name)
