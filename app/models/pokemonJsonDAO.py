from app.models.pokemon import Pokemon
from app import app
import json

class PokemonJsonDAO:

    pokemons = []
    def __init__(self):
        with open(app.static_folder+"/data/pokemons.json", "r", encoding="UTF-8") as f:
            PokemonJsonDAO.pokemons = json.load(f)

    def findAll(self):
        listAllPokemons = []
        for p in PokemonJsonDAO.pokemons:
            NewPokemon = Pokemon(p)
            listAllPokemons.append(NewPokemon)
        return listAllPokemons
    
    def findByNumber(self,numero):
        for p in PokemonJsonDAO.pokemons:
            if(p["Number"] == numero):
                return Pokemon(p)
        return []   

    def findByType(self,type):
        listOfType = []
        for p in PokemonJsonDAO.pokemons:
            if(p["Type_1"] == type):
                listOfType.append(Pokemon(p))
        return listOfType 

