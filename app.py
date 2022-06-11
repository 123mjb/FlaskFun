from flask import Flask,render_template
from random import randrange as r
app = Flask(__name__)
txtfile=open('words.txt')

@app.route("/")
def home():
    link1=[""]
    link2=[""]
    link3=[""]
    return render_template("index.html", thing=txtfile.readline(r(0,466550)))

if __name__ == '__main__':
    app.run(debug=True)
