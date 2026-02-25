from app import app
from flask import render_template,url_for,redirect,request
import json

class PokemonController:
    
    with open(app.static_folder+"/data/pokemons.json","r",encoding="UTF-8") as f:
        pokemons = json.load(f)
     
    @app.route("/pokemon/<int:pokedex_id>", methods=["GET"])    
    def pokemonView(pokedex_id):
        for p in PokemonController.pokemons:
            if(p["Number"] == pokedex_id):
                num = str(p["Number"])
                if len(num) == 1:
                    num = '00'+num
                elif len(num) == 2:
                    num = '0'+num
                img = url_for("static",filename="img/pokemons/"+num+".png")
                return render_template("pokemon.html",data = p ,img = img,page='index', metadata ={"title":'Pokemon view', "pagename":'pokemon'})
        return "<p>Pokemon inconnu</p>"
    
    @app.route("/pokemon", methods=["POST"])
    def pokemonByIndex():
        pokeType = request.form["typ"]
        if not(pokeType == ""):
            return redirect(url_for("pokemonByType",pokeType = pokeType))
        num = int (request.form["numero"])
        for p in PokemonController.pokemons:
            if(p["Number"] == num):
                num = str(p["Number"])
                if len(num) == 1:
                    num = '00'+num
                elif len(num) == 2:
                    num = '0'+num
                img = url_for("static", filename="img/pokemons/"+num+'.png')
                # return render_template("pokemon.html", data = p,img = img,index='true')
                return render_template("pokemon.html",data = p ,img = img,index='true', metadata ={"title":'Pokemon view', "pagename":'pokemon'})

        return "<p>numero invalide</p>"
    
    @app.route("/pokemon/type=<string:pokeType>", methods=["GET"])
    def pokemonByType(pokeType):
        liste = []
        for p in PokemonController.pokemons:
            if(p["Type_1"]==pokeType or p["Type_2"]==pokeType):
                num = str(p["Number"])
                if len(num) == 1:
                    num = '00'+num
                elif len(num) == 2:
                    num = '0'+num
                img = url_for("static", filename="img/pokemons/"+num+'.png')
                p["url"]= img
                liste.append(p)
        return render_template("pokemon.html",liste = liste,type = 'true', metadata ={"title":'Pokemons view', "pagename":'pokemon'})        
        # return render_template("pokemon.html",liste = liste,type = 'true')
                
        