# Decision Maker - Ivan Li

import random

num_inputs = 0
while True:
    try:
        num_inputs = int(input("How many choices are you making? "))
        break
    except ValueError:
        print("Please type a number...")

user_inputs = []
for i in range(num_inputs):
    user_input = (input(f"Enter value #{(i+1)}: "))
    user_inputs.append(user_input)

print(f"The final decision is: {random.choice(user_inputs).format()}")
