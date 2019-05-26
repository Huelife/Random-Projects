#inventory_check.py: Simple inventory check with 1 item

print("Let's check your inventory!")

#setting items in inventory list
inventory = ["sword","helmet","armor","shield","gun","boots","gloves"]

#while loop continues until user inputs 'check' string
while True:
  try:
    check = input("Type 'check' to check inventory. ")
  except ValueError:
    continue
  else:
    if check == "check":
#printing number of items in inventory list
      print("")
      print("You have {} items in your inventory.".format(len(inventory)))
      print("Let's check what you have: \n{}".format(inventory))
      print("")
      break
    else:
      print("{} is an invalid option.".format(check))
      continue
      
print("You've picked up (3) more swords! "
      "Let's check how many swords you have now!")

#creating add_sword function that adds 'sword' to inventory[1]
def add_sword():
  inventory.insert(1, "sword")
  
#three 'swords' are added to inventory list
add_sword()
add_sword()
add_sword()

#while loop continues until user inputs 'sword' string
while True:
  try:
    sword_value = input("Type 'sword' to check the total "
                        "number of swords in your inventory. ")
  except ValueError:
    continue
  else:
    if sword_value == "sword":
#entering 'sword' prints total number of 'swords' in inventory list
      print("")
      print("You have ({}) swords".format(inventory.count("sword")))
      break
    else:
      print("{} is an invalid option.".format(sword_value))
      continue
