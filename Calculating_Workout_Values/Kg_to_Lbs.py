print ("Let's convert pounds and kilograms!")
print ("")

while True:
  try:
    weight = float(input("How much weight would you like to convert? "))
  except ValueError:
    continue
  else:
    if weight <= 0:
      print("Please enter a value > 0")
      continue
    break
while True:
  try:
    units = input("Do you want to convert to lbs or kgs? ")
  except ValueError:
    continue
  else:
    if units in("lbs","LBS","lb","LB"):
      solution = weight * 2.20
      unit1 = "kgs"
      unit2 = "lbs"
    elif units in("kgs","KGS","kg","KG"):
      solution = weight / 0.45
      unit1 = "lbs"
      unit2 = "kgs"
    else:
      continue
    break
print("")
print("You converted " + str(weight) + " " + unit1 + " to " + str(solution) + " " + unit2)