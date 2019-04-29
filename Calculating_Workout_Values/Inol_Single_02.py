print("Let's figure out your INOL value!")
print("")

while True:
  try:
    weight = float(input("How much weight are you using?"))
  except ValueError:
    continue
  else:
    if weight <= 0:
      print("Weight should be greater than 0.")
      continue
    break
while True:
  try:
    perc = float(input("What % is this weight of your 1 rep max?"))
  except ValueError:
    continue
  else:
    if perc <= 0 or perc > 100:
      print("Percentage should be greater than 0, but less than or equal to 100.")
      continue
    break
while True:
  try:
    sets = int(input("How many sets did you do?"))
  except ValueError:
    continue
  else:
    if sets <= 0:
      print("Sets should be greater than 0.")
      continue
    break
while True:
  try:
    reps = int(input("How many reps did you do?"))
  except ValueError:
    continue
  else:
    if reps <= 0:
      print("Reps should be greater than 0.")
      continue
    break
if perc > 0 and perc <= 99:
  inol = (sets * reps) / (100.0 - perc)
elif perc > 99 and perc <= 100:
  inol = (sets * reps)
print("")
print("Your INOL is: " + str(round(float(inol),3)))
