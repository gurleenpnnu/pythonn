import random
name = input("Enter your name: ")
winning_score= int(input("Enter winning score(target to win): "))
choices = ["Rock", "Paper", "Scissors"]

def play_game():
 user = input(f"{name}, enter your choice: ").strip().lower()
 if user == "r":
    user = "Rock"
 elif user == "p":
    user = "Paper"
 elif user == "s":
    user = "Scissors"
 else:
    user = user.capitalize()

 if user not in choices:
    print("Invalid choice!")
    return None
 computer = random.choice(choices)

 print(f"{name}'s choice:  {user}" )
 print(f"Computer's choice: {computer}")


 if user == computer:
     print("It's a tie!")
     return "tie"
 elif user == "Scissors" and computer == "Paper":
    print("You won!")
    return "user"
 elif user == "Paper" and computer == "Rock":
    print("You won!")
    return "user" 
 elif user == "Rock" and computer == "Scissors":
    print("You won!")
    return "user"

 else:
    print("you lost, better luck next time ")
    return "computer" 

user_score = 0
computer_score = 0 
 
round_number = 1
while True:
  print(f"\n== Round {round_number}==")
  result= play_game()
  if result == "computer":
     computer_score +=1
  elif result == "user":
      user_score +=1

  print("\n---SCORE---")
  print(f"{name}'s score: {user_score}")
  print(f"Computer score: {computer_score}")


  if user_score ==winning_score :
     print("\n========================================")
     print("          ROCK PAPER SCISSORS")
     print("========================================")
     print(f"Congratulations! You are the overall winner {name}🏆!")
     print("Final Score")
     print("-----------")
     print(f"{name}: {user_score}")
     print(f"Computer: {computer_score}\n")
     print("Thanks for playing!")
     print("See you next time! 👋")
     print("========================================")
     break
  
  elif computer_score == winning_score :
     print("\n========================================")
     print("          ROCK PAPER SCISSORS")
     print("========================================")
     print(" WINNER: Computer 🏆\n")
     print("Final Score")
     print("-----------")
     print(f"{name}: {user_score}")
     print(f"Computer: {computer_score}\n")
     print("thanks for playing!")
     print("better luck next time! 👋")
     print("========================================")
     break


  again = input("Play again? (yes/no): ").lower()
  if again != "yes":
        break
  round_number += 1