from flask import render_template,redirect,url_for 
from app import app
import json
from app.services.PokemonService import PokemonService

class IndexController:
    
    pokemons = PokemonService()

@app.route("/", methods=["GET"])
def rentrer():
    return redirect("/index")

@app.route("/index", methods=["GET"])
def index():
    # on recupere la liste des types de pokemon pour notre liste deroulante
    liste = IndexController.pokemons.getPokemonTypes()
    return render_template("index.html", types = liste,metadata ={"title":'home Page', "pagename":'index'})