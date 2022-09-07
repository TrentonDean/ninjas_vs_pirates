import random

class Character:

    def __init__(self,name):                                                    # initialize the parent class Character
        self.health = 100
        self.name = name
        self.heal_counter = 2
        self.defense = 0

    def player_turn(self):                                                      # this lets us input the value for each players turn, which is returned
        choice_value = input(f"{self.name}! What would you like to do?\nEnter the number!\n1: Attack\n2: Buff Strength\n3: Agility\n4: Heal (Heals Remaining: {self.heal_counter})\n5: Buff Defense\n")
        return choice_value

    def buff(self):                                                             # this buffs the strength of the player by 4
        self.strength += 4
        print(f"--------------------\n{self.name}'s attack rose!\n--------------------")
        return self

    def show_stats( self ):                                                     # displays the players stats
        print(f"Name: {self.name}\nType: {self.type}\nStrength: {self.strength}\nSpeed: {self.speed}\nDefense: {self.defense}\nHealth: {self.health}\n--------------------")

    def attack ( self , player ):                                               # this attacks the other player with a small chance of a critical hit
        crit = random.randrange(1,100)
        if crit > 90:
            amount = (self.strength *1.5)
            player.health -= amount
            print(f"--------------------\n**A Critical Hit!!**\n{self.name} attacked {player.name} for {amount} damage!\n--------------------")
        else:
            amount = (self.strength - player.defense)
            player.health -= amount
            print(f"--------------------\n{self.name} attacked {player.name} for {amount} damage!\n--------------------")
            return self

    def agility(self):                                                          # this buffs the speed of the player by 3
        self.speed += 3
        print(f"--------------------\n{self.name}'s speed rose!\n--------------------")

    def heal(self):                                                             # each player is given 2 heals, this heals the player by 30 points while they have heals left
            self.heal_counter -= 1
            self.health += 30
            print(f"--------------------\n{self.name} healed 30 points!\n--------------------")

    def defend(self):                                                           # this buffs the defense by either 1, 2, 3, or 4, chosen randomly but with higher chances for lower numbers
        block = random.randrange(1, 100)
        
        if block < 40:
            self.defense += 1
            print(f"--------------------\n{self.name}'s defense slightly rose!\n--------------------")
        elif block > 40 and block < 70:
            self.defense += 2
            print(f"--------------------\n{self.name}'s defense rose!\n--------------------")
        elif block > 70 and block < 90:
            self.defense += 3
            print(f"--------------------\n{self.name}'s defense rose by a lot!\n--------------------")
        elif block > 90:
            self.defense += 4
            print(f"--------------------\n{self.name}'s defense insanely rose!\n--------------------")