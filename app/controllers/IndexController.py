from flask import render_template,redirect,url_for
from app import app
import json

class IndexController:
    
    with open(app.static_folder+"/data/pokemons.json","r",encoding="UTF-8") as f:
        pokemons = json.load(f)

@app.route("/", methods=["GET"])
def rentrer():
    return redirect("/index")

@app.route("/index", methods=["GET"])
def index():
    liste = []
    for p in IndexController.pokemons:
        if not(p["Type_1"] in liste ):
            liste.append(p["Type_1"])
        if not( p["Type_2"] in liste ):
            liste.append(p["Type_2"])
    return render_template("index.html", types = liste,metadata ={"title":'home Page', "pagename":'index'})