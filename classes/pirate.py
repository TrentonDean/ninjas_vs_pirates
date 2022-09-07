from classes import Character


class Pirate(Character):

    def __init__( self , name ):                            # initialize the child class Pirate
        super().__init__(name)
        self.strength = 15
        self.speed = 3
        self.type = "Pirate"