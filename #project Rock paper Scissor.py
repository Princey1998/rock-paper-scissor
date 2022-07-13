#project Rock paper Scissor
#rules of game
#Paper defeats Rock
#rock defeats scissor
#Scissor defeats paper

#condition of winning
#p= paper
#r= rock
#s= scissor
#Step1=take human input
#Step2=take computer input
#Step3=check who is the winner
#Step4=Add the source in the winner account
#Step5=ask if u want to repeat (y/n)


#step1
def takehumanInput():
    ch=input("Enter the value out of p/r/s - ")
    ch=ch.lower()
    if ch=='p' or ch=='r' or ch=='s':
        return ch
    else:
        return takehumanInput()
            
#step2= take computer input
import random
def generateComputerValue():
    ch =""
    n = random.randint(0,3)
    if n== 0:
      ch= 's'
    elif n == 1:
      ch = 'r' 
    else:
      ch = 'p'
    return ch

#check who is the winner
# p+r=p
# p+s=s
# r+s=r
# p+p=tie
# r+r=tie
# s+s=tie

def checkWinner(humanInput, ComputerInput):
  winner =""
  if humanInput == 'p' and ComputerInput == 'r':
    winner ="human"
  elif humanInput == 'p' and ComputerInput == 's':
    winner ="computer"
      
  elif humanInput == 'r' and ComputerInput == 's':
    winner ="human"
  elif humanInput == 'r' and ComputerInput == 'p':
    winner ="computer"
  elif humanInput == 's' and ComputerInput == 'r':
    winner ="computer"
  elif humanInput == 's' and ComputerInput == 'p':
    winner ="human"
  elif humanInput == 'p' and ComputerInput == 'r':
    winner ="Tie"
  elif humanInput == 'p' and ComputerInput == 'r':
    winner ="Tie"
  elif humanInput == 'r' and ComputerInput == 'r':
    winner ="Tie"
  else:
    winner ="Tie"   
  return winner
  #score
           

def updateScore(user):
  if user == "human":
    score["human"] = score.get("human")+1
  elif user =="computer":  
    score["computer"] = score.get("computer")+1
  else:
    score["tie"] = score.get("tie")+1

  updateScore()

  # Ask for Again play  
score = {"human":0, "computer":0, "tie":0}
playAgain = "y"
while playAgain != 'n':

 humanInput = takehumanInput()
print("Human Input is - ", humanInput)    
computerInput = generateComputerValue()
print("Computer Input is - ",computerInput)
winner = checkWinner(humanInput,computerInput)
print("Winner of the round is - ",winner)
updateScore(winner)
print("Updated score is - ",score)
playAgain = input("Do you want to play again y/n -")


