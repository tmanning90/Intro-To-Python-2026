#We will have 3 doors: 1 door is the winner
#The contestant picks one door, then the host opens a different door
#The contestant should change their option
#We reveal if the contestant the right door
import random

def Winners():

  winningDoor = random.randint(1,3) #pcks a random number 1-3
  contestantChoice = random.randint(1,3)

#print("Winner: " + str(winningDoor) + "; contestantChoice: " + str(contestantChoice))

  revealDoor = random.randint(1,3)
  while revealDoor == winningDoor or revealDoor == contestantChoice:
   revealDoor = random.randint(1,3)
#print("Winner: " + str(winningDoor) + "; contestantChoice: " + str(contestantChoice) + "; Host Opens Door #" + str(revealDoor))

  contestantFinal = random.randint(1,3)
  while contestantFinal == contestantChoice or contestantFinal == revealDoor:
    contestantFinal = random.randint(1,3)

  if contestantFinal == winningDoor:
    print("The contestant wins a brand new car!")
  else:
    print("No winners today.")

Winners = 0
for i in range(1000):
  win=Winners()
  if win:
    Winners +=1
print("Winners are " + str(Winners))

          
  
      
