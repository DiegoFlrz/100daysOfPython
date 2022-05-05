import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
#Write your code below this line 👇
# cant figure out how to also call the rock/paper/scissor symbols from above AND keep them a assigned variable
player1_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player1_move >= 3 or player1_move < 0:
    print("You typed an invalid number, You Lose.")
else:
    computer_choice = random.randint(0, 2)
    print()
    print("You chose: ")
    print(game_images[player1_move])
    print("Computer chose: ")
    print(game_images[computer_choice])

    if player1_move == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and player1_move == 2:
        print("You Lose!.")
    elif computer_choice > player1_move:
        print("You Lose!")
    elif player1_move > computer_choice:
        print("You Win!")
    elif computer_choice == player1_move:
        print("Its a draw.")

