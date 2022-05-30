from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<name>")
def home():
    return render_template('main.html',name2=name)

if __name__== '__main__':
    app.run(debug= True)