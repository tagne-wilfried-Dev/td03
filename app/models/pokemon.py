import math
from flask import url_for

class Pokemon:
    # methode pour convertir un numero de pokemon en chaine 
    # de 3 chiffres pour le nom de l'image
    def threeDigit(number):
        strNum = str(number)
        while len(strNum) < 3:
            strNum = '0'+strNum
        return strNum
    def __init__(self,dict):
        self.number=dict["Number"]
        self.name=dict["Name"]
        self.type=dict["Type_1"]
        self.hP=dict["HP"]
        self.attack=dict["Attack"]
        self.defense=dict["Defense"]
        self.spAttack=dict["Sp_Atk"]
        self.spDefense=dict["Sp_Def"]
        self.speed=dict["Speed"]
        self.generation=dict["Generation"]

    def getGlobalDefense(self):
        return self.hP*math.sqrt(self.defense*self.spDefense)
    
    def getGlobalAttack(self):
        return self.attack*self.spAttack
    
    # pour avoir l'url de l'img d'un pokemon
    def getUrl(self):
        return url_for("static", filename="img/pokemons/"+Pokemon.threeDigit(self.number)+".png")
    