import random
rand_num = random.randint(0,2)

if rand_num == 0:
 	computer =  "rock"
elif rand_num == 1:
	computer = "paper"	
else:
	computer = "scissors"

print("...rock...")
print("...paper...")
print("...scissors...")
player = input("player enters: ").lower()	
print(f"computer plays {computer}" )	
print("shoot")
if player:
	if player == 'rock' and computer == 'scissors':
		print("Player wins")
	elif player == 'rock' and computer == 'paper':
		print("computer wins")	
	elif player == 'paper' and computer == 'rock':
		print("Player wins")	
	elif player == 'paper' and computer == 'scissors':
		print("computer wins")
	elif player == 'scissors' and computer == 'rock':
		print("computer wins")	
	elif player == 'scissors' and computer == 'paper':
		print("Player wins")
	elif player == computer:
		print("it is a tie")		
	else:
		print("wrong!wrong!")			
else:
	print("you entered wrong choice.")	