import random
def rock_paper_scissors():            #Function Creation :Reuse the block of code ,by calling a function.
  choice=["rock","paper","scissors"]
  player_win=0
  computer_win=0
  tie=+0

  print("Rock")
  print("Paper")
  print("Scissors")
  while True:     # While Loop: While Loop runs as long as a condition is true.
     player=str(input("Select an option :")).lower()
     computer = random.choice(choice)
     print(f"You: {player}, Computer: {computer}")
 #Conditional Statement (elif) : If one condition is not satisfied its check with another(elif) condition ,if not prints else Statement.
     if player==computer:
         print("Tie!..")
         tie=+1
     elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
          print("You win!")
          player_win += 1
     elif(player not in choice):
          print("Invalid choice")
     else:
          print("Computer win")
          computer_win+=1
     print("Player count is:",player_win)
     print("Computer count is:",computer_win)
     print("Ties,:",tie)
rock_paper_scissors()  # Calling a Function
