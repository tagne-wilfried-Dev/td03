import math
class Pokemon:
    
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

    def getGobalDefense(self):
        return self.hP*math.sqrt(self.defense*self.spDefense)
    
    def getGlobalAttack(self):
        return self.attack*self.spAttack
    