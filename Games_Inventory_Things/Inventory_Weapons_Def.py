print("Choose your weapon!")
print("")
#creating weapon_list list
weapon_list = ["Legendary Sword", "Legendary Shield", "Legendary Gun", "Legendary Bow", "Legendary Axe"]
print(weapon_list)
print("")
#declaring functions that print item stats associated with weapon_list list
def Leg_Sw():
  print ("You've chosen the Legendary Sword!")
  print ("Stats: +100 STR, +50 AGI, +50 SPD")
def Leg_Sh():
  print ("You've chosen the Legendary Shield!")
  print ("Stats: +200 DEF, +200 VIT, +200 RES")
def Leg_Gu():
  print ("You've chosen the Legendary Gun!")
  print ("Stats: +100 PIE, +100 AGI, +200 SPD")
def Leg_Bo():
  print ("You've chosen the Legendary Bow!")
  print ("Stats: +100 RNG, +200 AGI, +100 SPD")
def Leg_Ax():
  print ("You've chosen the Legendary Axe!")
  print ("Stats: +200 STR, +50 VIT, +25 AGI")

#while loop continues until user inputs 'Quit'
while True:
  try:
    weapon = input("Enter a number from 1-5 to see weapon name and attributes, otherwise, enter 'Quit' to leave")
  except ValueError:
    continue
  else:
    if weapon == "Quit":
      break
    elif weapon == "1":
      print ("")
      Leg_Sw()
      print ("")
    elif weapon == "2":
      print ("")
      Leg_Sh()
      print ("")
    elif weapon == "3":
      print ("")
      Leg_Gu()
      print ("")
    elif weapon == "4":
      print ("")
      Leg_Bo()
      print ("")
    elif weapon == "5":
      print ("")
      Leg_Ax()
      print ("")
    continue
