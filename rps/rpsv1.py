print("...rock...")
print("...paper...")
print("...scissors...")
player1 = input("player 1 enters: ")
player2 = input("player 2 enters: ")
print("shoot")
if player1 and player2:
	if player1 == 'rock' and player2 == 'scissors':
		print("Player 1 wins")
	elif player1 == 'rock' and player2 == 'paper':
		print("Player 2 wins")	
	elif player1 == 'paper' and player2 == 'rock':
		print("Player 1 wins")	
	elif player1 == 'paper' and player2 == 'scissors':
		print("Player 2 wins")
	elif player1 == 'scissors' and player2 == 'rock':
		print("Player 2 wins")	
	elif player1 == 'scissors' and player2 == 'paper':
		print("Player 1 wins")
	elif player1 == player2:
		print("it is a tie")		
	else:
		print("wrong!wrong!")			
else:
	print("you entered wrong choice.")															