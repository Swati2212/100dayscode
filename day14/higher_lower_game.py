from art import logo, vs
from game_data import data
import random

def format_data(account):
  """Takes the account data and return the printable format."""
  account_name = account['name']
  account_desc = account['description']
  account_country = account['country']
  return (f"{account_name}, a {account_desc} from {account_country}")

##Use if statement to check if the user is in correct format
def check_answer(guess, a_follower_count, b_follower_count):
  """check if statement to check if the user is correct."""
  if a_follower_count > b_follower_count:
    return guess == "a"
  else:
    return guess == "b"

#display art
print(logo)
score = 0
account_b = random.choice(data)

#make the game repetable
game_should_conutine = True
while game_should_conutine:
  #Generate a random account from the data

  #Making account at position B at the next account at position A.

  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)
  print(f"Compare A: {(format_data(account_a))}")
  print(vs)
  print(f"Against B: {(format_data(account_b))}")

  #Ask users for a guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  ##get the followers count of each account
  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  #give user the feedback on their guess
  if is_correct:
    #score keeping
    score += 1
    print(f"You're right! Current Score: {score}")
  else:
    game_should_conutine = False
    print(f"Sorry that's wrong.Final score: {score}")








