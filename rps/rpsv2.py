print("...rock...")
print("...paper...")
print("...scissors...")
player1 = input("player 1 enters: ")
print("***No Cheating***\n\n" * 20)

player2 = input("player 2 enters: ")
print("shoot")
if player1 and player2:
	if player1 == player2:
		print("it is a tie")
	elif player1 == 'rock':  
		if player2 == 'scissors':
			print("Player 1 wins")
		elif player2 == 'paper':
			print("Player 2 wins")	
	elif player1 == 'paper':
		if player2 == 'rock':
			print("Player 1 wins")	
		elif player2 == 'scissors':
			print("Player 2 wins")
	elif player1 == 'scissors': 
		if player2 == 'rock':
			print("Player 2 wins")	
		elif player2 == 'paper':
			print("Player 1 wins")	
	else:
		print("wrong!wrong!")			
else:
	print("you entered nothing")															