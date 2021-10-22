import random

inp = input("Player 1, choose your weapon [Rock, Paper, or Scissor]: ")
player_one = inp.upper()
weapon: list[str] = ["PAPER", "ROCK", "SCISSOR"]
player_two = random.choice(weapon)

if player_one == "ROCK":
    if player_two == "SCISSOR":
        print("Player TWO chose", player_two, "to bring to the fight.")
        print("Player ONE you WIN!")
    elif player_two == "PAPER":
        print("Player TWO chose", player_two, "to bring to the fight.")
        print("Player ONE you LOSE!")
    elif player_two == "ROCK":
        print("Player TWO chose", player_two, "to bring to the fight.")
        print("The clash ends in a DRAW")
    else:
        print("Player TWO chose", player_two, "to bring to the fight.")
        print("Choice INVALID")
if player_one == "PAPER":
    if player_two == "ROCK":
        print("Player TWO chose", player_two, "to bring to the fight.")
        print("Player ONE you WIN!")
    elif player_two == "SCISSOR":
        print("Player TWO chose", player_two, "to bring to the fight.")
        print("Player ONE you LOSE!")
    elif player_two == "PAPER":
        print("Player TWO chose", player_two, "to bring to the fight.")
        print("The clash ends in a DRAW")
    else:
        print("Player TWO chose", player_two, "to bring to the fight.")
        print("Choice INVALID")
if player_one == "SCISSOR":
    if player_two == "PAPER":
        print("Player TWO chose", player_two, "to bring to the fight.")
        print("Player ONE you WIN!")
    elif player_two == "ROCK":
        print("Player TWO chose", player_two, "to bring to the fight.")
        print("Player ONE you LOSE!")
    elif player_two == "SCISSOR":
        print("Player TWO chose", player_two, "to bring to the fight.")
        print("The clash ends in a DRAW")
    else:
        print("Player TWO chose", player_two, "to bring to the fight.")
        print("Choice INVALID")
