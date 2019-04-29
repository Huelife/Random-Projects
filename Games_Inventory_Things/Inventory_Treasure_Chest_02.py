from random import randint

stats = {"Damage": [300, 2, 3],"Agility": [150, 5, 5],"Speed": [150, 5, 5],}

pickup_random = 0

while True:
  try:
    pickup = input("Do you want to open the treasure chest?")
  except ValueError:
    print("Please choose 'yes' or 'no'.")
    continue
  else:
    if pickup == "yes":
      pickup_random = randint(0,10)
      if pickup_random in (0,1,4,6,8,9,10):
        print("Found: Sword A!")
        print(stats)
      elif pickup_random in (2,5,7):
        stats["Damage"] = [220, 2, 2]
        stats["Agility"] = [190, 8, 8]
        stats["Speed"] = [190, 8, 8]
        print("Found: Sword B!")
        print(stats)
      elif pickup_random == 3:
        stats["Damage"] = [150, 1, 1]
        stats["Agility"] = [300, 10, 10]
        stats["Speed"] = [300, 10, 10]
        print("Found: Sword C!")
        print(stats)
      else:
        continue
      break
    elif pickup == "no":
      break
    else:
      print("Please choose 'yes' or 'no'.")
      continue