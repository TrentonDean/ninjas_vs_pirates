from classes.ninja import Ninja                             # Importing the different modules
from classes.pirate import Pirate
from classes import __init__
import time                                                 # Allows the use of 'time'

def choice(self,choice_value):                              # this function takes the choice_value returned from the player_turn function, and chooses what to do based on that input     
    if choice_value == "1":
        if self == player1:                                 # decides which player to attack
            self.attack(player2)
        elif self == player2:
            self.attack(player1)
    elif choice_value == "2":
        self.buff()
    elif choice_value == "3":
        self.agility()
    elif choice_value == "4":
        if self.heal_counter > 0:
            self.heal()
        elif self.heal_counter == 0:
            print("No Heals Remaining!\n--------------------")
            choice(self,self.player_turn())
    elif choice_value == "5":
        self.defend()
    elif choice_value == "6":
        if self == player1:                                 # decides which player to attack
            if self.type == "Pirate":
                player1.scurvy(player2)
            elif self.type == "Ninja":
                player1.shuriken(player2)
        elif self == player2:
            if self.type == "Pirate":
                player2.scurvy(player1)
            elif self.type == "Ninja":
                player2.shuriken(player1)
        
    else:
        print("--------------------\nPlease make a valid choice")# insurance to keep the game going
        choice(self,self.player_turn())

def game():                                                 # main function, decides turn order based on speed          
    for i in range(1,100):
        win = 1
        print(f"TURN {i}!\n--------------------")

        if i == 1:                                          # first turn, since you just saw the stats I didn't want to shove them in your face again
            if player1.speed > player2.speed:
                win = check()                               # runs check() to see if someone won
                if win == 0:
                    break
                else: pass
            
                choice(player1,player1.player_turn())
                time.sleep(1.5)                             # so you have a second to read

                win = check()
                if win == 0:
                    break
                else: pass

                choice(player2,player2.player_turn())
                time.sleep(1.5)
            elif player2.speed > player1.speed:
                win = check()
                if win == 0:
                    break
                else: pass

                choice(player2,player2.player_turn())
                time.sleep(1.5)

                choice(player1,player1.player_turn())
                time.sleep(1.5)

                win = check()
                if win == 0:
                    break
                else: pass

        else:                                               # every turn after 1
            player1.show_stats()                                        
            player2.show_stats()

            if player1.speed > player2.speed:
                win = check()
                if win == 0:
                    break
                else: pass
                
                choice(player1,player1.player_turn())
                time.sleep(1.5)

                win = check()
                if win == 0:
                    break
                else: pass

                choice(player2,player2.player_turn())
                time.sleep(1.5)
            elif player2.speed > player1.speed:

                choice(player2,player2.player_turn())
                time.sleep(1.5)

                win = check()
                if win == 0:
                    break
                else: pass

                choice(player1,player1.player_turn())
                time.sleep(1.5)

                win = check()
                if win == 0:
                    break
                else: pass

def check():                                                # if health falls below 0 returns 0
    if player1.health <= 0:
        print(f"{player2_name} won! {player2_type}s kick ass!!\n--------------------")
        return 0
    elif player2.health <= 0:
        print(f"{player1_name} won! {player1_type}s kick ass!!\n--------------------")
        return 0
    else:
        pass

print("--------------------")                               # Using 'input()' to take in Player 1's name and preferred team
player1_name = input("Enter Player 1 Name: ")
print("--------------------")
player1_type = input("Wanna be a Pirate or a Ninja? ")
print("--------------------")
if player1_type == "Pirate" or player1_type == "pirate":
    player1_type = "Pirate"
    player1 = Pirate(player1_name)
elif player1_type == "Ninja" or player1_type == "ninja":
    player1_type = "Ninja"
    player1 = Ninja(player1_name)
else:                                                       # by default, if given a type that's not 'ninja' or 'pirate', you will be a 'ninja'
    print("INVALID CHOICE\nDEFAULT TO NINJA")
    player1_type = "Ninja"
    player1 = Ninja(player1_name)
player1.show_stats()

player2_name = input("Enter Player 2 Name: ")               # Initialize Player 2, and they will be whatever team player 1 is not
print("--------------------")
if player1_type == "Ninja":
    player2_type = "Pirate"
    print(f"Since {player1_name} is a {player1_type}, {player2_name} will be a {player2_type}")
    player2 = Pirate(player2_name)
elif player1_type == "Pirate":
    player2_type = "Ninja"
    print(f"Since {player1_name} is a {player1_type}, {player2_name} will be a {player2_type}")
    player2 = Ninja(player2_name)
player2.show_stats()

time.sleep(3)                                               # waits 3 seconds before continuing so the players have a second to view stats

game()                                                      # runs the game