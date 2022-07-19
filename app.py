from flask import Flask,render_template,g,request
from random import randrange as r
import sqlite3

DATABASE = './static/database.db'
app = Flask(__name__)
txtfile=open('words.txt')

link_link=["/Info","/","/games","/Login"]
link_name=["Info","Homepage","Games","Login"]
link_description=["Description and makers","Main page with everything","Some Games","Login"]

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
    global link_link,link_name,link_description
    username = request.args.get('username')
    try:
        q=username
    except NameError:
        username = None
    text = [f"Hello Codename {username}","Welcome back to **redacted**","Below are links to the important sites.","Use responsibly"]
    return render_template("index.html", user=username,links2= [i + f"?username={username}" for i in link_link] if username != None else link_link, link_name2=link_name,link_description2=link_description,lines=text)

@app.route("/Info")
def info():
    global link_link,link_name,link_description
    username = request.args.get('username')
    try:
        q=username
    except NameError:
        username = None
    text = ["I made it :)","Now go do something important or cool. ༼ つ ◕_◕ ༽つ"]
    return render_template("index.html",links2= [i + f"?username={username}" for i in link_link] if username != None else link_link, link_name2=link_name,link_description2=link_description,lines=text)

@app.route("/games")
def gamesfunc():
    gamesnames=["undergarf","moomoo","lordz","Minecraft","Github"]
    gameslocs=["https://v6p9d9t4.ssl.hwcdn.net/html/5957883/index.html","https://moomoo.io/?adlt=strict&toWww=1&redig=CCB7B1F83172457296444BD3273EE65A","https://lordz.io/","https://yexex.github.io/eagle/index.html","https://Github.com"]
    return render_template("game.html",games=[gamesnames,gameslocs])



@app.route("/Login",methods=['GET', 'POST'])
def search(): 
    global link_link, link_name, link_description
    qry = request.args.get('username')
    cur = get_db().cursor()
    try:
        q=qry
    except NameError:
        qry = None
        information = None
    if qry != None:
        if cur.execute(f"SELECT EXISTS(SELECT INFO FROM USERS WHERE USERNAME = '{qry}');").fetchone():
                information = cur.execute(f"SELECT INFO FROM USERS WHERE USERNAME = '{qry}';").fetchone()[0]
        else: information = None
    else: information = None
    return render_template("Login.html", query=qry, info=information, links2= [i + f"?username={qry}" for i in link_link] if qry != None else link_link, link_name2=link_name)
    
if __name__ == '__main__':
    app.run(debug=True)
