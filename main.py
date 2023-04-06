from flask import Flask, render_template, request, redirect, url_for

app = Flask(
	__name__,
	template_folder='templates',
	static_folder='static')

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/spare")
def spare():
    return render_template("sparetemplate.html")

if __name__ == "__main__":
	app.run(
		host='0.0.0.0',
		debug=True
	)