from classes import Character


class Ninja(Character):

    def __init__( self , name ):                    # initialize the child class Ninja
        super().__init__(name)
        self.strength = 10
        self.speed = 5
        self.type = "Ninja"

    def shuriken(self,player):
        amount = (self.strength - player.defense) + 3
        player.health -= amount
        print(f"--------------------\n{self.name} threw a shuriken at {player.name} for {amount} damage!\n--------------------")
        return self