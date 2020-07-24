import random

money = 100


def coin_flip (bet_amount, heads_or_tails):
  result = random.randint(0,1)
  if (result == 0):
    print ("Heads")
  elif (result == 1):
    print ("Tails")


    if (result == 0 and heads_or_tails == "Heads") or (result == 1 and heads_or_tails == "Tails"):
      print("You win " + str(bet_amount))
    elif (result == 1 and heads_or_tails == "Heads") or (result == 0 and heads_or_tails == "Tails"): 
      print("You lose -" + str(bet_amount))
    else:
      print("It was a tie, try again...")




def rolling_dice(bet_amount, odd_or_even):
  die_1 = random.randint(1, 6)
  die_2 = random.randint(1, 6)
  result = die_1 + die_2

  if (result % 2 == 0 and odd_or_even == "Even") or (result % 2 == 1 and odd_or_even == "Odd"):
    print("You win " + str(bet_amount))
  else: 
    print("You lose -" + str(bet_amount))




def highest_card_wins(bet_amount, card_drawn):
  card_1 = random.randint(1, 10)
  card_2 = random.randint(1, 10)

  if (card_1 > card_2):
    print("You win " + str(bet_amount))
  elif (card_1 < card_2):
    print("You lose -" + str(bet_amount))
  else:
    print("It was a tie, try again...")




def roulette(bet_amount, prediction):
number = random.randint(0,36)
if (number = 0):
  print("It has landed on 0")

  if (prediction == "Even") and (number % 2 == 0):
    print("You win! It landed on " + str(bet_amount))
  elif (prediction == "Odd") and (number % 2 == 1):
    print("You win! It landed on " + str(bet_amount))
  elif (prediction = number):
    print("Spot On! You win " + str(number * 35)
  else:
    print("You lose, try again...")



def roulette():
  number = random.dandint(0,36)
