"""
tbcstart.py

@author: michael.scott
"""
import random

class Character(object):
    
    def __init__(self, name = "default name", hitPoints = 10, hitChance = 60, maxDamage = 3, armor = 2):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.armor = armor
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        value = self.testInt(value, 0, 100, 0)
        self.__hitPoints = value
        
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        value = self.testInt(value, 0, 100, 0)
        self.__armor = value
        
    @property
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        value = self.testInt(value, 0, 100, 0)
        self.__hitChance = value
    
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        value = self.testInt(value, 0, 100, 0)
        self.__maxDamage = value
        
    def testInt(self, value, min = 0, max = 100, default = 0):
        """ takes in value 
        checks to see if it is an int between
        min and max.  If it is not a legal value
        set it to default """

        out = default
    
        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value 
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")
    
        return out

    def printStats(self):
        print (f"""
 {self.name}
 hit points: {self.hitPoints}
 hit chance: {self.hitChance}
 max damage: {self.maxDamage}
 armor: {self.armor}""")
     
    def hit(self, enemy):
        hitRand = random.randint(0, 100)
        dmgNum = random.randint(1, self.maxDamage)
        if hitRand <= self.hitChance:
            print(f"""{self.name} hits {enemy.name}
                        for {dmgNum} points of damage
                        {enemy.name}'s armor absorbs {enemy.armor} points of damage
              """)
            if dmgNum > enemy.armor:
                dealtDmg = dmgNum - enemy.armor
                enemy.hitPoints -= dealtDmg
        else:
            print(f"{self.name} missed")
    
def fight(player, enemy):
    keepGoing = True
    while keepGoing:

        player.hit(enemy)
        enemy.hit(player)

        print(f"{player.name}: {player.hitPoints} HP")
        print(f"{enemy.name}: {enemy.hitPoints} HP")

        if player.hitPoints > 0:
            if enemy.hitPoints > 0:
                userChoice = input("Press ENTER for another round or Q to quit: ")
                if userChoice == "Q":
                    keepGoing = False
            else:
                print(f"{player.name} wins")
                keepGoing = False
        else:
            print(f"{enemy.name} wins")
            keepGoing = False
        
                

              


def main():
      c = Character("jim", 20, 99)
      m = Character()
      c.printStats()
    
    
    



if __name__ == "__main__":
    main()
