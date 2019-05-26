#calculating_mpg.py: Mpg based on mileage, gallons, driving conditions

#importing decimal and round values
from decimal import Decimal, ROUND_UP, ROUND_DOWN

print("Let's calculate city/highway mpg!")
print("")

#gathering input from user for miles, gallons, and city percentage driving
while True:
  try:
    distance = float(input("How many miles did you travel? "))
  except ValueError:
    print("Not a number!")
    continue
  else:
    if distance <= 0:
      print("Please enter a number > 0.")
      continue
    break
    
while True:
  try:
    gallons = float(input("How many gallons did you use? "))
  except ValueError:
    print("Not a number!")
    continue
  else:
    if gallons <= 0:
      print("Please enter a number > 0.")
      continue
    break
    
while True:
  try:
    city_per = float(input("What percentage of city driving did you do? "))
  except ValueError:
    print("Not a number!")
    continue
  else:
    if city <= 0:
      print("Please enter a number > 0.")
      continue
    break
    
print("")

#calculating and rounding values
mpg = distance / gallons
mpg_round = Decimal(str(mpg)).quantize(Decimal('.1'))
highway_per = 100.0 - city_per

city100 = 0.857 * mpg
highway100 = mpg / 0.807

city100_round = (Decimal(str(city100)).quantize
            (Decimal('.1'),rounding=ROUND_UP))
highway100_round = (Decimal(str(highway100)).quantize
               (Decimal('.1'),rounding=ROUND_DOWN))

#printing current mpg, and city and highway percentage
print("Your mpg is: {}.".format(mpg_round))
print("You drove: {}% city/{}% highway.".format(city_per,highway_per))
print("")

#printing mpg if user drives 100% city or 100% highway
print("If you drove 100% city, your mpg would be: {}.".format(city100_round))
print("If you drove 100% highway, your mpg would be: {}.".format(highway100_round))
