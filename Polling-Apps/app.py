from flask import Flask, render_template, redirect, url_for, request,session
from models import User,db
app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

@app.route("/home")
def home():
	return "Hello"

@app.route("/register", methods=["POST","GET"])
def register():
	error = None
	if request.method == "POST":
		if request.form["username"] == "" or request.form["email"] == "":
			error="Masukkan dengan benar, masukkan username dan umur anda"
		else:
			return redirect(url_for("home"))
		
	return render_template('login.html', error=error)
	#create new record in database
	user = User(nama_lengkap=nama_lengkap,
				email=email)
	db.session.add(user)
	db.session.commit()	
if __name__=="__main__":
	app.run()