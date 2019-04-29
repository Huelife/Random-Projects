#importing randint
from random import randint

#rules and info for user
print("Let's play 21!")
print("""Rules are simple:
           First to 21 wins!
           If not, higher number wins!
           Over 21 loses...""")
print("")
print("--"*20)

#value of cards and image of cards displayed
cards_letters = [0,"A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
cards_numbers = [0,1,2,3,4,5,6,7,8,9,10,10,10,10]
#things I want to add later
# if dealer = 16-21 stay
#    hitme = input("Type HITME to add card, otherwise, type STAY")
#    if hitme == "HITME":

you = 0

#while loop that continues until 'you' variable is '1' or more
while True:
  try:
    play = input("Press enter to play! ")
  except ValueError:
    continue
  else:
#when user presses enter key, game begins and 4 random rolls from 1-13 are created
    if play == "":
      roll_one = randint(1,13)
      roll_two = randint(1,13)
      dealer_roll_one = randint(1,13)
      dealer_roll_two = randint(1,13)
      
 #setting value of 1 for user and dealer
      if roll_one == 1 and roll_two == 1:
        cards_numbers[roll_two] = 11
      elif roll_one == 1:
        cards_numbers[roll_one] = 11
      elif roll_two == 1:
        cards_numbers[roll_two] = 11
      elif dealer_roll_one == 1 and dealer_roll_two == 1:
        cards_numbers[dealer_roll_two] = 11
      elif dealer_roll_one == 1:
        cards_numbers[dealer_roll_one] = 11
      elif dealer_roll_two == 1:
        cards_numbers[dealer_roll_two] = 11

#setting total value of cards for dealer and user
      your_total = cards_numbers[roll_one] + cards_numbers[roll_two]
      dealer_total = cards_numbers[dealer_roll_one] + cards_numbers[dealer_roll_two]

#printing playing card images and total, using the created lists, based on the random numbers created for user and dealer
      print("You: [" + str(cards_letters[roll_one]) + "]" + "[" + str(cards_letters[roll_two]) + "]" + " = " + str(your_total))
      print("Dealer: [" + str(cards_letters[dealer_roll_one]) + "]" + "[" + str(cards_letters[dealer_roll_two]) + "]" + " = " + str(dealer_total))
      print("")

#determining if user wins, wins with black jack, loses, or if it's a draw
#user only gets 1 chance, unless it's a draw. Game repeats for draws until user wins or loses
      if your_total == 21 and dealer_total < 21:
        you += 1
      elif your_total == dealer_total:
        print("DRAW!")
        continue
      elif your_total <= 21 and dealer_total > 21:
        you += 1
      elif your_total > dealer_total and your_total <= 21:
        you += 1
      break
    else:
      continue
    break
#message that appears at the end to show if the user wins, wins with black jack, or loses
if you >= 1 and your_total == 21:
  print("Black Jack! CONGRATULATIONS! YOUVE WON!")
elif you >=1:
  print("CONGRATULATIONS! YOUVE WON!")
else:
  print("Sorry... You lose...")