from flask import Flask, redirect, url_for

#create instance of flask web app
app = Flask(__name__)
#define home page, path of the func in web:wq!
@app.route("/")
def home():
	return"Hello world"
#page accept param
@app.route("/<name>")
def user(name):
	return f"hello {name}"
@app.route("/admin")
def admin():
	return redirect(url_for("home"))

if __name__ == "__main__":
	app.run()
