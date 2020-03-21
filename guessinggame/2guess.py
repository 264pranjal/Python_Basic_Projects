import random
rand_num = random.randint(0,10)
guess = None
while guess != rand_num:
	guess = input("Guess the number between 0 to 10: ")
	guess = int(guess)

	if guess < rand_num:
		print("too low,try again")
	elif guess > rand_num:
		print("too high,try again")
	else:
		print("you won")	
print(rand_num)		