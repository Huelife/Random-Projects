#INOL stands for Intensity Number Of Lifts
print("Let's figure out your INOL value!")
print("")
#while loop continues until a float value > 0 is entered
#fluff code from lines 7-16, not used in the end and deletable
while True:
  try:
    weight = float(input("How much weight are you using? "))
  except ValueError:
    continue
  else:
    if weight <= 0:
      print("Weight should be greater than 0.")
      continue
    break
#while loop continues until a float value > 0, but less than 100, is entered
while True:
  try:
    perc = float(input("What % is this weight of your 1 rep max? "))
  except ValueError:
    continue
  else:
    if perc <= 0 or perc > 100:
      print("Percentage should be greater than 0, but less than or equal to 100.")
      continue
    break
#while loop continues until an int value > 0 is entered
while True:
  try:
    sets = int(input("How many sets did you do? "))
  except ValueError:
    continue
  else:
    if sets <= 0:
      print("Sets should be greater than 0.")
      continue
    break
#while loop continues until an int value > 0 is entered
while True:
  try:
    reps = int(input("How many reps did you do? "))
  except ValueError:
    continue
  else:
    if reps <= 0:
      print("Reps should be greater than 0.")
      continue
    break
#INOL is calculated and rounded with 2 different equations, one for: 0 < perc <= 99; and 99 < perc <= 100. No perc > 100 taken
#INOL requires user input for: weight, perc, sets, and reps. Weight value is not used in the current equations
if perc > 0 and perc <= 99:
  inol = round(float((sets * reps) / (100.0 - perc)),3)
elif perc > 99 and perc <= 100:
  inol = (sets * reps)
#INOL value printed
print("")
print("Your INOL is: {}".format(inol))
