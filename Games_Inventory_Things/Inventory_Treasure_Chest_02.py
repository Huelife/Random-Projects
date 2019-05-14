#simple treasure chest game with 3 items
#importing randint for random values
from random import randint

#stats dictionary for 'Damage', 'Agility', and 'Speed' with values
stats_a = {"Damage:": [300, 2, 3],"Agility:": [150, 5, 5],"Speed:": [150, 5, 5],}
stats_b = {"Damage:": [220, 2, 2],"Agility:": [190, 8, 8],"Speed:": [190, 8, 8],}
stats_c = {"Damage:": [150, 1, 1],"Agility:": [300, 10, 10],"Speed:": [300, 10, 10],}

pickup_random = 0

#while loop continues until user input is 'no'
while True:
  try:
    pickup = input("Please choose 'yes' or 'no'.\nDo you want to open the treasure chest? ")
  except ValueError:
    continue
  else:
#probability of Sword A > Sword B > Sword C
    if pickup == "yes":
      pickup_random = randint(0,10)
      if pickup_random in (0,1,4,6,8,9,10):
        print("_"*25)
        print("Found: Sword A!")      
        for stats_column in stats_a:
          print(" ",stats_column,stats_a[stats_column])
        print("_"*25)
      elif pickup_random in (2,5,7):
        print("_"*25)
        print("Found: Sword B!")
        for stats_column in stats_b:
          print(" ",stats_column,stats_b[stats_column])
        print("_"*25)
      elif pickup_random == 3:
        print("_"*25)
        print("Found: Sword C!")
        for stats_column in stats_c:
          print(" ",stats_column,stats_c[stats_column])
        print("_"*25)
    elif pickup == "no":
      break
    continue
