print("...rock...")
print("...paper...")
print("...scissors...") 
import random
rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"            
player1 = input("Enter your choice\n").lower()
print(computer)
if (player1=="rock" and computer == "scissors") or (player1 == "paper" and computer == "rock") or (player1=="scissors" and computer == "paper"):
    print("Player1 wins");
elif player1 == computer:
    print("Its a tie")
elif (computer=="rock" and player1 == "scissors") or (computer == "paper" and player1 == "rock") or (computer=="scissors" and player1 == "paper"):
    print("Computer wins");
else:
    print("Something went wrong")            