from random import randint

print("Let's play a dice game!")
print("""Rules are simple: 
       The higher roll wins.
       3 turns wins game.
       < 3 wins by 5 turns loses.""")
print("")

turn = 0
wins = 0
while True:
  try:
    print("-"*30)
    print("Turn", turn + 1)
    play = input("Press enter to play. ")
  except ValueError:
    continue
  else:
    if play == "":
      turn += 1
      roll_one = randint(1,6)
      roll_two = randint(1,6)
      roll_total = roll_one + roll_two
      dealer_roll_one = randint(1,6)
      dealer_roll_two = randint(1,6)
      dealer_roll_total = dealer_roll_one + dealer_roll_two

      print("Your roll: [" + str(roll_one) + "]" +"[" + str(roll_two) + "] = " + str(roll_total))
      print("Dealer roll: [" + str(dealer_roll_one) + "]" +"[" + str(dealer_roll_two) + "] = " + str(dealer_roll_total))
    
      if roll_total > dealer_roll_total:
        wins += 1
        print("You win!")
        print("")
        if wins == 3 and turn <= 5:
          break
        elif wins < 3 and turn == 5:
          break
        else:
          continue
      elif roll_total < dealer_roll_total:
        print("You lose...")
        print("")
        if wins < 3 and turn == 5:
          break
        else: 
          continue
      elif roll_total == dealer_roll_total:
        print("Draw!")
        print("")
        if wins < 3 and turn == 5:
          break
        else: 
          continue
      else:
        print("You lose...")
        print("")
        if wins < 3 and turn == 5:
          break
        else: 
          continue
    else:
      continue
if wins >= 3:
    print("--"*20)
    print("CONGRATULATIONS! YOUVE WON THE GAME!!!")
else:
    print("--"*20)
    print("Sorry... Youve lost the game...")