#inventory_weapons_def.py: Weapon stats using functions and print

#declaring functions that print item stats associated with weapon_list list
def Leg_Sw():
  print("You've chosen the Legendary Sword!")
  print("Stats: +100 STR, +50 AGI, +50 SPD")
  
def Leg_Sh():
  print("You've chosen the Legendary Shield!")
  print("Stats: +200 DEF, +200 VIT, +200 RES")
  
def Leg_Gu():
  print("You've chosen the Legendary Gun!")
  print("Stats: +100 PIE, +100 AGI, +200 SPD")
  
def Leg_Bo():
  print("You've chosen the Legendary Bow!")
  print("Stats: +100 RNG, +200 AGI, +100 SPD")
  
def Leg_Ax():
  print("You've chosen the Legendary Axe!")
  print("Stats: +200 STR, +50 VIT, +25 AGI")

print("Choose your weapon!")
print("")

#creating weapon_list list and weapon_list_02 dict
weapon_list = ["Legendary Sword","Legendary Shield","Legendary Gun",
               "Legendary Bow","Legendary Axe"]

#weapon_list_02 dict
weapon_list_02 = {
  "1":Leg_Sw,
  "2":Leg_Sh,
  "3":Leg_Gu,
  "4":Leg_Bo,
  "5":Leg_Ax
}

#for loop printing all items in weapon_list
for i in weapon_list:
  print(i)
print("")

#while loop continues until user inputs 'Quit'
while True:
  try:
    weapon = input("Enter a number from 1-5 to see weapon name and "
                   "attributes, otherwise,\nenter 'Quit' to leave. ")
  except ValueError:
    continue
  else:
    if weapon == "Quit":
      break
    elif weapon in ("1","2","3","4","5"):
      print("")
      weapon_list_02[weapon]()
      print("")
    else:
      print("{} is an invalid option.".format(weapon))
    continue
