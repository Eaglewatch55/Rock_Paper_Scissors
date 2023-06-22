# Write your code here
import random
#random.seed(10)

while True:
    user_input = input()

    if user_input == "!exit":
        print("Bye!")
        break

    lose_dict = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    options = ["rock", "paper", "scissors"]
    comp_choice = random.choice(options)

    if lose_dict.get(user_input) == comp_choice:
        print(f"Sorry, but the computer chose {lose_dict[user_input]}")
    elif user_input == comp_choice:
        print(f"There is a draw {user_input}")
    elif lose_dict.get(comp_choice) == user_input:
        print(f"Well done. The computer chose {comp_choice} and failed")
    else:
        print("Invalid input")
