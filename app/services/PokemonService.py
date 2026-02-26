from app.models.pokemonJsonDAO import PokemonJsonDAO as PokemonDAO

class PokemonService:
    # pokemonDAO = None
    pokemonDAO = PokemonDAO()
    def __init__():
        PokemonService.pokemonDAO = PokemonDAO()

    def getPokemonByNumber(self,number):
        pokemon = PokemonService.pokemonDAO.findByNumber(number) 
        if(pokemon == []):
            return pokemon
        else:
            return [pokemon]
    
    def getPokemonTypes(self,type):
        pokemons = PokemonService.pokemonDAO.findAll()
        listTypes = []
        for p in pokemons:
            if p.type not in listTypes:
                listTypes.append(p.type)
        return listTypes
    
    def getPokemonByType(self,type):
        listOfType = PokemonService.pokemonDAO.findByType(type)
        if(listOfType == []):
            return [{}]
        else:
            return listOfType
