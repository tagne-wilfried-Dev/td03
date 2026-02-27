from app.models.pokemonJsonDAO import PokemonJsonDAO as PokemonDAO

class PokemonService:
    
    pokemonDAO = PokemonDAO()
    def __init__():
        PokemonService.pokemonDAO = PokemonDAO()

    def getPokemonByNumber(self,number):
        pokemon = PokemonService.pokemonDAO.findByNumber(number) 
        if(pokemon == []):
            return pokemon
        else:
            return [pokemon]
    
    def getPokemonTypes(self):
        pokemons = PokemonService.pokemonDAO.findAll()
        typesList = []
        for p in pokemons:
            if p.type not in typesList:
                typesList.append(p.type)
        return typesList
    
    def getPokemonByType(self,type):
        listOfType = PokemonService.pokemonDAO.findByType(type)
        if(listOfType == []):
            return [{}]
        else:
            return listOfType
