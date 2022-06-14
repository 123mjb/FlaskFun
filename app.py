from flask import Flask,render_template
from random import randrange as r
app = Flask(__name__)
txtfile=open('words.txt')

link_link=["/Info","/","/games"]
link_name=["Info","Homepage","Games"]
link_description=["Description and makers","Main page with everything","Some Games"]

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
if __name__ == '__main__':
    app.run(debug=True)
