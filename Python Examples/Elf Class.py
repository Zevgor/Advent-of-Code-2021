import json

#defines Elf class

class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str": 11, "dex": 12, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]

#defines default Elf object
playerelf = Elf(level=4)
print(playerelf.hp,playerelf.ability_scores["str"])

#defines elf with overridden ability scores
newelf = Elf(level=5,ability_scores={"str":12,"dex":15,"con":14,"int":20,"wis":14,"cha":13})
print(newelf.hp,newelf.ability_scores["str"])