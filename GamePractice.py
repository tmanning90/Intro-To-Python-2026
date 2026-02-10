import os, time #library operating system and libray time. Time delays print like older video games.

def slowText(text, delay=0.015): #this slows down the printed code
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  #this function gives the pace of the printed words

def start(): #purpose of start function: the beg. of game, gets playerName variable
    global playerName #establishes playerName as a gloabal variable, not just in that function.
    os.system('cls' if os.name == 'nt' else 'clear') #nt means nothing? #purpose of os import - typing for the computer to do something / clears the screen automatically throughout the game.
    slowText("Welcome to the game! Please enter your name: ")
    playerName = input() #this is a variable
    slowText("Hello, {}! You find yourself in the living room of a mysterious house.".format(playerName))
    slowText("From here, you can go to the kitchen, the bedroom, or the garden.")
    # Further game logic would go here
    livingRoom() #this function tells you where you are and gives choices of where to go (other variables)

def livingRoom(): #continuation of the start and allows player to go to living room
    global backpack
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("You are in the living room. There are doors to the kitchen, bedroom, and garden. You can also look for items.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "kitchen":
        kitchen() #underlined because the kitchen function does not exist yet
    elif choice == "bedroom":
        bedroom()
    elif choice == "garden":
        garden()
    elif choice == "look for items":
        if searchBackpack(backpack, "oreos"):
            slowText("You decided to scan the room, and you found nothing.")
        else:    
            slowText("You decided to scan the room. You find a half-eaten pack of oreos. Do you want to pick them up?")
            choice = input().strip().lower
            if choice == "yes":
                backpack.append("oreos")
                print(backpack) # this line is only for testing
        time.sleep(2)    
        livingRoom() 
    else:
        print("Invalid choice. Please try again.")
        time.sleep(3)
        livingRoom() #inputs a choice of functions of what room the players chooses.
#creating a kitchen

def kitchen(): 
    global backpack
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("You are in the kitchen. There is a door to the living room.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "livingRoom":
        livingRoom() 
    else:
        print("Invalid choice. Please try again.")
        livingRoom() 

def garden(): 
    global backpack
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("You are in the garden. There is a door to the living room.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "livingRoom":
        livingRoom() 
    else:
        print("Invalid choice. Please try again.")
        livingRoom() 

def bedroom(): 
    global backpack
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("You are in the bedroom. There is a door to the living room.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "livingRoom":
        livingRoom() 
    else:
        print("Invalid choice. Please try again.")
        livingRoom() 

def searchBackpack(pack, item):
    #this function should return true if item is inside the list named 'pack'
    found = False
    for i in range(len(pack)):
        if pack[i] == item:
            found = True
    return found
playerName = ""
backpack = []
start()
