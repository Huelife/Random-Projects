from decimal import Decimal

print("Let's figure out your daily INOL value!")
print("")

sets = ("first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth")

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

inol_add = 0

for x in range(sets_total):
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
  while True:
    try:
      warmup_rep = int(input("How many reps in your " + sets[x] + " warmup?"))
    except ValueError:
      continue
    else:
      if warmup_rep <= 0:
        print("Reps should be greater than 0.")
        continue
      elif warmup_percentage > 0 and warmup_percentage <= 99:
        warmup_inol = (warmup_set * warmup_rep) / (100.0 - warmup_percentage)
      elif warmup_percentage > 99 and warmup_percentage <= 100:
        warmup_inol = (warmup_set * warmup_rep)
      swarmup_inol = Decimal(str(warmup_inol)).quantize(Decimal('.001'))
      inol_add += swarmup_inol
      print("")
      print("INOL: " + str(swarmup_inol))
      print("")
      break
print("Total warmup INOL: " + str(inol_add))