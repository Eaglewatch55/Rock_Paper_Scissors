# Write your code here
import random
import os
#random.seed(10)


def read_scores(filename):
    score_dict = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    name, score = line.strip().split()
                except ValueError:
                    continue
                score_dict[name] = int(score)

        return score_dict

    except IndexError:
        return dict()


def save_scores(score_dict: dict, p_name, increment: int):
    newline = os.linesep
    try:
        score_dict[p_name] += increment
    except KeyError:
        score_dict[p_name] = increment

    to_save = [" ".join([p[0], str(p[1])]) for p in score_dict.items()]
    with open("rating.txt", "w", newline="\n") as f:
        for line in to_save:
            f.write(line)

    return


def print_result(result: str, obj: str):
    p_dict = {"Win": f"Well done. The computer chose {obj} and failed",
              "Draw": f"There is a draw ({obj})",
              "Loss": f"Sorry, but the computer chose {obj}"}
    print(p_dict[result])


def game(game_type, name, s_dict, option_list=None):
    while True:
        user_input = input()

        if user_input == "!exit":
            print("Bye!")
            exit()
        elif user_input == "!rating":
            try:
                print("Your rating:", int(s_dict[name]))
            except KeyError:
                print("Your rating: 0")
            finally:
                continue

        increment = game_type(user_input, option_list)

        if increment is not None:
            save_scores(s_dict, name, increment)


def traditional_game(choice, z):
        lose_dict = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
        options = ["rock", "paper", "scissors"]
        comp_choice = random.choice(options)

        if lose_dict.get(choice) == comp_choice:
            print_result("Loss", lose_dict[choice])
            return None

        elif choice == comp_choice:
            print_result("Draw", choice)
            return 50

        elif lose_dict.get(comp_choice) == choice:
            print_result("Win", comp_choice)
            return 100

        else:
            print("Invalid input")
            return None


#CHECK INDEXES. ITS MAKING ERRORS
def variable_game(choice, option_list: list):
    comp_choice = random.choice(option_list)

    try:
        win_list, loss_list = calculate_relations(option_list.index(choice), option_list[:])
    except ValueError:
        pass

    if comp_choice == choice:
        print_result("Draw", choice)
        return 50

    #print(win_list, loss_list)

    if comp_choice in win_list:
        print_result("Win", comp_choice)
        return 100
    elif comp_choice in loss_list:
        print_result("Loss", comp_choice)
        return None
    else:
        print("Invalid input")
        return None


def calculate_relations(choice, options: list):
    compensate = lambda c: c - (0 if c < len(options) else len(options))
    wins = []
    loses = []
    options.pop(choice)

    for i in range(len(options)):
        index = i + choice

        if i < len(options) / 2:
            wins.append(options[compensate(index)])
        else:
            loses.append(options[compensate(index)])

    return wins, loses


player = input("Enter your name: ")
print("Hello,", player)
scores = read_scores("rating.txt")

option_input = input()
print("Okay, let's start")

if option_input == "":
    game(traditional_game, player, scores)
else:
    game(variable_game, player, scores, option_input.split(","))



