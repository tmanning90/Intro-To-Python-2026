import os, time #library operating system and libray time. Time delays print like older video games.

def slowText(text, delay=0.1): #this slows down the printed code
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
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("You are in the living room. There are doors to the kitchen, bedroom, and garden.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "kitchen":
        kitchen() #underlined because the kitchen function does not exist yet
    elif choice == "bedroom":
        bedroom()
    elif choice == "garden":
        garden()
    else:
        print("Invalid choice. Please try again.")
        livingRoom() #inputs a choice of functions of what room the players chooses.
#creating a kitchen


playerName = ""
start()
