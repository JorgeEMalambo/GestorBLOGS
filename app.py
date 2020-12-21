from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    pagetitle = "HomePage"
    return render_template("registro-blogs.html",
                            mytitle=pagetitle,
                            mycontent="Hello World")