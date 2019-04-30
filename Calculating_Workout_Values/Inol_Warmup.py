#importing decimal for rounding
from decimal import Decimal

#INOL stands for Intensity Number Of Lifts
print("Let's figure out your daily INOL value!")
print("")

#sets tuple created with 12 possible values that can be called
sets = ("first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth")

#while loop created to determine total sets. While loop continues until user inputs an int > 0, but less than 13 
while True:
  try:
    sets_total = int(input("How many warmup sets do you have?"))
  except ValueError:
    continue
  else:
    if sets_total <= 0:
      print("No 0 or negative sets!")
      continue
    elif sets_total > 12:
      print("12 max sets!")
      continue
    break

#inol_add created so inol value gets added based on total number of sets
inol_add = 0

#for loop created, program loops based on total sets from user input
for x in range(sets_total):
#while loop continues until user inputs a float value > 0
  while True:
    try:
      warmup_weight = float(input("What's your " + sets[x] + " warmup weight?"))
    except ValueError:
      continue
    else:
      if warmup_weight <= 0:
        print("Weight should be greater than 0.")
        continue
      break
#while loop continues until user inputs a float value > 0 and <= 100
  while True:
    try:
      warmup_percentage = float(input("What's your " + sets[x] + " warmup percentage of your 1 rep max?"))
    except ValueError:
      continue
    else:
      if warmup_percentage <= 0 or warmup_percentage > 100:
        print("Percentage should be greater than 0, but less than or equal to 100.")
        continue
      break
#while loop continues until user inputs an int value > 0
  while True:
    try:
      warmup_set = int(input("How many sets in your " + sets[x] + " warmup?"))
    except ValueError:
      continue
    else:
      if warmup_set <= 0:
        print("Sets should be greater than 0.")
        continue
      break
#while loop continues until user inputs an int value > 0
  while True:
    try:
      warmup_rep = int(input("How many reps in your " + sets[x] + " warmup?"))
    except ValueError:
      continue
    else:
      if warmup_rep <= 0:
        print("Reps should be greater than 0.")
        continue
#inol value is calculated with two different formulas: 1) for 0 < perc value <= 99, and 2) for 99 < perc value <= 100
#no perc value > 100 used
#inol value for current set is also rounded to 0.001 decimal and printed
      elif warmup_percentage > 0 and warmup_percentage <= 99:
        warmup_inol = (warmup_set * warmup_rep) / (100.0 - warmup_percentage)
      elif warmup_percentage > 99 and warmup_percentage <= 100:
        warmup_inol = (warmup_set * warmup_rep)
      swarmup_inol = Decimal(str(warmup_inol)).quantize(Decimal('.001'))
#inol for current set is added to inol_add
      inol_add += swarmup_inol
      print("")
      print("INOL: " + str(swarmup_inol))
      print("")
      break
#total inol value from each added set is printed
print("Total warmup INOL: " + str(inol_add))
