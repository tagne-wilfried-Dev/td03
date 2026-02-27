from flask import render_template,redirect,url_for
from app import app

@app.route("/info", methods=["GET"])
def info():
    #permet d'utiliser le template jinja "index.html"
    # avec les donnees data dans la variable data (ce nom sera alors utilise dans le template)
    return render_template("info.html", metadata ={"title":'Info Page', "pagename":'info'})