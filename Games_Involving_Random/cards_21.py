#cards_21.py: Card game playing 21/Black Jack

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
cards_letters = (0,"A",2,3,4,5,6,7,8,9,10,"J","Q","K")
cards_num = [0,1,2,3,4,5,6,7,8,9,10,10,10,10]
cards_num2 = [0,1,2,3,4,5,6,7,8,9,10,10,10,10]
cards_num3 = [0,1,2,3,4,5,6,7,8,9,10,10,10,10]
cards_num4 = [0,1,2,3,4,5,6,7,8,9,10,10,10,10]

#things I want to add later
# if dealer = 16-21 stay
#    hitme = input("Type HITME to add card, otherwise, type STAY")
#    if hitme == "HITME":

win = 0

#while loop that continues until 'you' variable is '1' or more
while True:
  try:
    play = input("Press enter to play! ")
  except ValueError:
    continue
  else:
#game begins with 4 random rolls from 1-13 when user presses enter
    if play == "":
      roll_one = randint(1,13)
      roll_two = randint(1,13)
      dealer_roll_one = randint(1,13)
      dealer_roll_two = randint(1,13)  
           
 #setting value of 1 for user and dealer
      if roll_one == 1 and roll_two == 1:
        cards_num[roll_one] = 11
        cards_num2[roll_two] = 1        
      elif roll_one == 1 and roll_two != 1:
        cards_num[roll_one] = 11
      elif roll_two == 1 and roll_one != 1:
        cards_num2[roll_two] = 11
      if dealer_roll_one == 1 and dealer_roll_two == 1:
        cards_num3[dealer_roll_one] = 11
        cards_num4[dealer_roll_two] = 1
      elif dealer_roll_one == 1 and dealer_roll_two != 1:
        cards_num3[dealer_roll_one] = 11
      elif dealer_roll_two == 1 and dealer_roll_one != 1:
        cards_num4[dealer_roll_two] = 11

#setting total value of cards for dealer and user
      your_total = cards_num[roll_one] + cards_num2[roll_two]
      dealer_total = cards_num3[dealer_roll_one] + cards_num4[dealer_roll_two]

#printing playing card images and total, using the created lists
      print("You: [{}][{}] = {}".format(cards_letters[roll_one],
            cards_letters[roll_two],your_total))
      print("Dealer: [{}][{}] = {}".format(cards_letters[dealer_roll_one],
            cards_letters[dealer_roll_two],dealer_total))
      print("")
           
#determining if user wins, wins with black jack, loses, or if it's a draw
#Game repeats for draws until user wins or loses
      if your_total == 21 and dealer_total < 21:
        win += 1
      elif your_total == dealer_total:
        print("DRAW!")
        continue
      elif your_total <= 21 and dealer_total > 21:
        win += 1
      elif your_total > dealer_total and your_total <= 21:
        win += 1

    else:
      print("{} is an invalid option.".format(play))
      continue
    break

#printing if user wins or loses
if win >= 1 and your_total == 21:
  print("Black Jack! CONGRATULATIONS! YOUVE WON!")
elif win >=1:
  print("CONGRATULATIONS! YOUVE WON!")
else:
  print("Sorry... You lose...")
