import random
def main():
	dice_sum = 0
	dice_rolls = int(input("How many dice you want to roll"))
	dice_size = int(input("How many sides you want to roll"))
	for i in range(0,dice_rolls):
		roll = random.randint(1,dice_size) #random.randint(1,6)  randint function gives random int in the following range (1,6)
		dice_sum += roll
		if roll == 1:
			print(f"You rolled a {roll}, critical fail")
		elif roll == dice_size:
			print(f"You rolled a {roll}, critical success")
		else:
			print(f"You rolled a {roll}")
		print(f'You rolled a {roll}')
	print(f"You have rolled a total of {dice_sum}")
if __name__== "__main__":
	main()

