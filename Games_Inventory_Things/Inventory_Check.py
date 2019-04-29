print("Let's check your inventory!")

inventory = ["sword","helmet","armor","shield","gun","boots","gloves"]
while True:
  try:
    check = input("Type 'check' to check inventory.")
  except ValueError:
    continue
  else:
    if check == "check":
      print("")
      print("You have "+str(len(inventory))+" items in your inventory.")
      print("Let's check what you have: "+str(inventory))
      print("")
      break
    else:
      continue
print("You've picked up (3) more swords! Let's check how many swords you have now!")
def add_sword():
  inventory.insert(1, "sword")
add_sword()
add_sword()
add_sword()
while True:
  try:
    sword_value = input("Type 'sword' to check the total number of swords in your inventory.")
  except ValueError:
    continue
  else:
    if sword_value == "sword":
      print("")
      print ("You have ("+str(inventory.count("sword"))+") swords")
      break
    else:
      continue