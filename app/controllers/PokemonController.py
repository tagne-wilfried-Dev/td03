from app import app
from flask import render_template,url_for,redirect,request
import json
from app.services.PokemonService import PokemonService
class PokemonController:
    
    pokemons = PokemonService()

    # afficher les details d'un pokemon selon son numero par get !!mais pas utilise
    @app.route("/pokemon/<int:pokedex_id>", methods=["GET"])    
    def pokemonView(pokedex_id):
        p = PokemonController.pokemons.getPokemonByNumber(pokedex_id)
        if p != []:
            return render_template("pokemon.html",data = p,index='true', metadata ={"title":'Pokemon view', "pagename":'pokemon'})
        else:
            return "<p>Pokemon inconnu</p>"
    
    # afficher les details d'un pokemon selon son numero
    @app.route("/pokemon", methods=["POST"])
    def pokemonByIndex():
        pokeType = request.form["typ"]
        if not(pokeType == ""): # rediriger vers pokemon type si le type est defini
            return redirect(url_for("pokemonByType",pokeType = pokeType))
        try: # gere le cas ou on soumet sans entrer de valeur
            num = int (request.form["numero"])
            p = PokemonController.pokemons.getPokemonByNumber(num)
            if p == []:
                return "<p>numero invalide</p>"
            # la variable index permet de faire savoir a pokemon.html s'il s'agit d'un affichage par indexe
            return render_template("pokemon.html",liste = p, index='true', metadata ={"title":'Pokemon view', "pagename":'pokemon'})
        except ValueError as e:
            return redirect("/index") # on reste sur la meme page s'il n'ya pas d'entree
        

    # afficher les pokemons d'un type precis
    @app.route("/pokemon/pokemontype=<string:pokeType>", methods=["GET"])
    def pokemonByType(pokeType):
        pokemonList = PokemonController.pokemons.getPokemonByType(pokeType)
        # la variable index permet de faire savoir a pokemon.html s'il s'agit d'un affichage par indexe
        return render_template("pokemon.html",liste = pokemonList,type = 'true', metadata ={"title":'Pokemons view', "pagename":'pokemon'})        

        
                
        