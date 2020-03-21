print("...rock...")
print("...paper...")
print("...scissors...")
player1 = input("Enter your choice\n").llower()
print("***No cheating!!\n"*20)
player2 = input("Enter your choice\n").lower()
if (player1=="rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1=="scissors" and player2 == "paper"):
    print("Player1 wins");
elif player1 == player2:
    print("Its a tie")
elif (player2=="rock" and player1 == "scissors") or (player2 == "paper" and player1 == "rock") or (player2=="scissors" and player1 == "paper"):
    print("Player2 wins");
else:
    print("Something went wrong")            