# Decision Maker - Ivan Li

import random

# Chooses the number of choices to randomly choose upon
num_inputs = 0
while True:
    try:
        num_inputs = int(input("How many choices are you making? "))
        break
    except ValueError:
        print("Please type a number...")

# Collects the input from user to choose upon
user_inputs = []
for i in range(num_inputs):
    user_input = (input(f"Enter choice #{(i+1)}: "))
    user_inputs.append(user_input)

final_decision = random.choice(user_inputs)
print(f"{final_decision} has been randomly selected")
