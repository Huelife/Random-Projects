print ("Let's convert pounds and kilograms!")
print ("")
#while loop continues until a float value > 0 is given
while True:
  try:
    weight = float(input("How much weight would you like to convert? "))
  except ValueError:
    print("Not a number!")
    continue
  else:
    if weight <= 0:
      print("Please enter a value > 0")
      continue
    break
#while loop continues until a string that is either lbs or kgs is chosen
while True:
  try:
    units = input("Do you want to convert to 'lbs' or 'kgs'? ").lower()
  except ValueError:
    continue
  else:
#user input can be 4 different iterations of lbs
#converting kgs value to lbs
    if units in("lbs","lb","l","ls"):
      solution = weight * 2.20
      unit1 = "kgs"
      unit2 = "lbs"
#user input can be 4 different iterations of kgs
#converting lbs value to kgs
    elif units in("kgs","kg","k","ks"):
      solution = weight / 0.45
      unit1 = "lbs"
      unit2 = "kgs"
    else:
      print("{} is not a valid choice.".format(units))
      continue
    break
#printing initial weight with units and converted weight with units
print("")
print("You converted {} {} to {} {}.".format(weight,unit1,solution,unit2))
