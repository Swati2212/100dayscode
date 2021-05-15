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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
games_images = [rock, paper, scissor]
user_choice = int(input("What do you choose? Type 0 for 'rock, 1 for 'paper', 2 for 'scissor'\n"))
if user_choice >= 3 or user_choice < 0 :
    print("You typed an invalid integer, You lose!")
else:
    print(f"You chose:{user_choice}")
    print(games_images[user_choice])


    computer_choose = random.randint(0,2)
    print(f"Computer chose: {computer_choose}")
    print(games_images[computer_choose])



    if user_choice == computer_choose:
        print("Draw")
    elif user_choice == 0 and computer_choose == 1:
        print("Computer Wins!")
    elif user_choice == 1 and computer_choose == 2:
        print("Computer Wins!")
    elif user_choice == 2 and computer_choose == 0:
        print("Computer Wins!")
    elif user_choice == 1 and computer_choose == 0:
        print("You Win!")
    elif user_choice == 0 and computer_choose == 2:
        print("You win!")
    else:
        print("You Win!")
