import random
rand_num = random.randint(0,10)
guess = None
while True:
	guess = input("Guess the number between 0 to 10: ")
	guess = int(guess)

	if guess < rand_num:
		print("too low,try again")
	elif guess > rand_num:
		print("too high,try again")
	else:
		print("you won")	
		play_again = input("Do you want to play again(y/n)? ")
		if play_again == "y":
			random_number = random.randint(1,10)  # numbers 1 - 10
			guess = None
		else:
			print("Thank you for playing")
			break	