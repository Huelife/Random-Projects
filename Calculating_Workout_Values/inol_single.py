#inol_single.py: Prints a single INOL value based on user input

#INOL stands for Intensity Number Of Lifts
print("Let's figure out your INOL value!")
print("")

#while loop continues until a float value > 0 is entered
#fluff code from lines 7-19, not used in the end, commented out for now
#while True:
#  try:
#    weight = float(input("How much weight are you using? "))
#  except ValueError:
#    print("Not a number!")
#    continue
#  else:
#    if weight <= 0:
#      print("Weight should be greater than 0.")
#      continue
#    break
    
#while loop continues until a float value > 0, but less than 100, is entered
while True:
  try:
    perc = float(input("What % is this weight of your 1 rep max? "))
  except ValueError:
    print("Not a number!")
    continue
  else:
    if perc <= 0 or perc > 100:
      print("Percentage should be > 0, but <= 100.")
      continue
    break
    
#while loop continues until an int value > 0 is entered
while True:
  try:
    sets = int(input("How many sets did you do? "))
  except ValueError:
    print("Not a number!")
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
    print("Not a number!")
    continue
  else:
    if reps <= 0:
      print("Reps should be greater than 0.")
      continue
    break
    
#INOL is calculated and rounded with 2 different equations
if perc > 0 and perc <= 99:
  inol = round(float((sets * reps) / (100.0 - perc)),3)
elif perc > 99 and perc <= 100:
  inol = (sets * reps)
  
#INOL value printed
print("")
print("Your INOL is: {}.".format(inol))
