from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("home.html")

@app.route("/home.html")
def home():
	return render_template("home.html")

@app.route("/about.html")
def about():
	return render_template("about.html")

@app.route("/resume.html")
def resume():
	return render_template("resume.html")

@app.route("/projects.html")
def projects():
	return render_template("projects.html")

@app.route("/contact.html")
def contact():
	return render_template("contact.html")

if __name__ == "__main__":
	app.run(debug = True)