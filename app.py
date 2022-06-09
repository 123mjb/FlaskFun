from flask import Flask,render_template
from random import randrange as r
app = Flask(__name__)
app.debug = True
@app.route("/")
def home():
    return render_template("index.html", randnum = r(0,r(0,1000000)))
