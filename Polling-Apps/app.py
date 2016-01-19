from flask import Flask, session,redirect,render_template,request,url_for
from models import User,db
import sys

app=Flask(__name__)
app.config.from_object('config')

reload(sys)
sys.setdefaultencoding("utf8")

db.init_app(app)

@app.route('/',methods=["POST","GET"])
def register():
	if request.method=="POST":
		nama_lengkap = request.form.get("nama_lengkap", None)
		email = request.form.get("email",None)
		if not validation([nama_lengkap, email]):
			error = 'too stupid'
			return render_template("login.html",**locals())

		user = User(nama_lengkap,email)
		db.session.add(user)
		db.session.commit()
		return 'something'

	return render_template("login.html", **locals())

def validation(fields):
	for loop in fields:
		if loop is None or loop == "":
			return False

	return True
if __name__=="__main__":
	app.run()
