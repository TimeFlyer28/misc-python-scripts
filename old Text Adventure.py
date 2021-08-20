

                                                        # My Text Adventure Game



# Imports

import random  #Needed for the Random Generator to Work
import sys  #Needed for game to end
import time  #Needed for time
import msvcrt  #For key input reader


# Dictionaries and Functions

player = {'name':'', 'lives':10, 'wood':0, 'metal':0, 'gold':0, 'diamonds':0, 'money':0}


def player_stats():

    print(f"{player['name']} {player['name']}'s Status:'")
    print(f"\nLives: {player['lives']}")
    print(f"Wood: {player['wood']}")
    print(f"Metal: {player['metal']}")
    print(f"Gold: {player['gold']}")
    print(f"Diamonds: {player['diamonds']}")
    print(f"Money: {player['money']}")


def choose_name():
    
    while player['firstname'] == "":

        print("Choose a Name:")
        print('\n')
        player['firstname'] = input("First Name?: ")

        if player['firstname'] != "":
            break
    
    
def life_generation(life_list):

    heart_update = random.choice(life_list)

    player['lives'] = player['lives'] + heart_update

    if player['lives'] > 0:

        if heart_update > 0:

            print(f"you gained {heart_update} lives")
        
        elif heart_update < 0:

            print(f"you lost {-1*heart_update} lives")

        elif heart_update == 0:

            print("Your life count was not affected")

        print(f"You currently have {player['lives']} lives left")

        input("\nPress Enter to continue...")
    
    elif player['lives'] <= 0:

        print(f"you lost {-1*heart_update} lives and are out of lives")

        print("\nGame Over")
        
        Player_Score()

        sys.exit



def chance_generator(chance_list):

    global Yes_No
    
    Yes_No = random.choice(chance_list)

        

def Player_Score():

    print("Can only be done after the rest of the game design is finished")






#________________________________________Life Events____________________________________________________________________________

Tree_Fall = [-5, -3, -2, -1]

Prickly_Bush = [-3, -2, -1]





#__________________________________________The Actual Game_______________________________________________________________________


print("\n\nWelcome to the Text Adventure 1.0")
print("By Anish Reddy")
print("07/02/2019")

print("\n")
print("\n")

choose_name()

print("\n")

input("Press enter to begin...")

print("\n\n\n\n")

print("You open your eyes to see the stars of the vast galaxy above you")

time.sleep(2)

print("You look around to see yourself on a strange, dark planet, scattered about with trees within the twilight...")

time.sleep(2)

print("In the distance, you can narrowly make out the silhouette of a small hut, shielded by trees and darkness...")

time.sleep(2)

print("You make your way towards the hut...")

time.sleep(1)

print("\n")

input('Press enter to continue')

print("\n")

Hazard_1 = [0, 0, 0, 1, 2]

chance_generator(Hazard_1)

if Yes_No == 1:

    print("On your way to the hut, an old eroding tree collapses on the ground, collapsing right on your head")

    life_generation(Tree_Fall)

elif Yes_No == 2:

    print("On your way to the hut, you stumble over a branch and fall into a prickly bush")

    life_generation(Prickly_Bush)


input()