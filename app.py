from flask import Flask,render_template
from random import randrange as r
app = Flask(__name__)
txtfile=open('words.txt')

link_link=["/Info","/"]
link_name=["Info","Homepage"]
link_description=["Description and makers","Main page with everything"]

@app.route("/")
def home():
    cname = txtfile.readline(r(0,466550))
    global link_link,link_name,link_description
    text = [f"Hello Codename {cname}","Welcome back to **redacted**","Below are links to the important sites.","Use responsibly"]
    return render_template("index.html", thing=cname,links=[link_link,link_name,link_description],lines=text)

@app.route("/Info")
def info():
    global link_link,link_name,link_description
    text = ["I made it :)"]
    return render_template("index.html",links=[link_link,link_name,link_description],lines=text)

if __name__ == '__main__':
    app.run(debug=True)
