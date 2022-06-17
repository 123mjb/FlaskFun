from flask import Flask,render_template,g
from random import randrange as r
import sqlite3

DATABASE = '/static/database.db'
app = Flask(__name__)
txtfile=open('words.txt')

link_link=["/Info","/","/games"]
link_name=["Info","Homepage","Games"]
link_description=["Description and makers","Main page with everything","Some Games"]

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def home():
    cname = txtfile.readline(r(0,466550))
    global link_link,link_name,link_description
    text = [f"Hello Codename {cname}","Welcome back to **redacted**","Below are links to the important sites.","Use responsibly"]
    return render_template("index.html", thing=cname,links=[link_link,link_name,link_description],lines=text)

@app.route("/Info")
def info():
    global link_link,link_name,link_description
    text = ["I made it :)","Now go do something important or cool."]
    return render_template("index.html",links=[link_link,link_name,link_description],lines=text)

@app.route("/games")
def gamesfunc():
    gamesnames=["undergarf","moomoo","lordz","Minecraft"]
    gameslocs=["https://v6p9d9t4.ssl.hwcdn.net/html/5957883/index.html","https://moomoo.io/?adlt=strict&toWww=1&redig=CCB7B1F83172457296444BD3273EE65A","https://lordz.io/","https://yexex.github.io/eagle/index.html"]
    return render_template("game.html",games=[gamesnames,gameslocs])

@app.route("/search")
@app.route("/search/<qry>")
def search():
    if qry != None:
        cur = get_db().cursor()
    return render_template("search.html", query=qry)
    
if __name__ == '__main__':
    app.run(debug=True)
