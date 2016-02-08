from flask import Flask, session,redirect,render_template,request,url_for
from models import User,db,Pilihan
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
		if nama_lengkap == "" or email == "":
			error = 'masukkan nama lengkap dan email secara benar'
			return render_template("registrasi.html",**locals())
		user = User(nama_lengkap,email)
		db.session.add(user)
		db.session.commit()
		#simpan user.id di session
		session["user_id"]=user.id
		#membatasi bnyaknya user yang memiliha
		if user.id ==11:
			return redirect("/hasil")
		elif user.id > 10:
			error = "user yang melakukan polling sudah cukup"
			return render_template("registrasi.html", **locals())
		return redirect("/polling")
	return render_template("registrasi.html", **locals())

@app.route('/polling',methods=["POST","GET"])
def polling():
	if request.method=="POST":
		python = request.form.get("python",None)
		go = request.form.get("go",None)
		user_id= session.get("user_id",None)
		if python  == "python":
			polls = Pilihan(user_id,python)
			db.session.add(polls)
			db.session.commit()
		else:
			polls = Pilihan(user_id,go)
			db.session.add(polls)
			db.session.commit()
		return redirect("/")
	return render_template("polling.html")

@app.route("/hasil")
def hasil():
	user = User.query.all()
	polls=Pilihan.query.all()
	return render_template("hasil.html", **locals())

if __name__=="__main__":
	app.run()
