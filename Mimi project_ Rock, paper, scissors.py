#               The Game of Rock, Paper, and Scissors


import random
choices = ["rock", "paper", "scissors"]

computer_choice = random.choice(choices)



computer_wins = 0
player_wins = 0



while computer_wins < 2 and player_wins < 2:
    

    print("              ")
    print("              ")
    print("Let's play rock, paper, or scissors")

    print("              ")

    player_choice = input("Rock, Paper, or Scissors? ").lower()

    print("              ")

    print(f"Computer chose: ", computer_choice)




    if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper" ) or (player_choice == "paper" and computer_choice == "rock"):
        winner = "Player"

    elif player_choice == computer_choice:
        
        winner = "Tie"
      
    else:
        
        winner = "Computer"



    if winner == "Player":
        print("              ")
        print("You win!!!")
        computer_wins += 1

    elif winner == "Computer":
        print("              ")
        print("Computer wins" , "hahaha !!!")
        computer_wins += 1

    else:
        print("              ")
        print("It is a tie")


    print("              ")
    print(f"Current score -                     Player: {player_wins}, Computer: {computer_wins}")


if player_wins > computer_wins:
    print("              ")
    print("              ")
    print("Congratulations! You won")

if not player_wins > computer_wins:
    print("              ")
    print("              ")
    print("Computer won! Better luck next time")



