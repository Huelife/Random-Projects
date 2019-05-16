#importing decimal and round values
from decimal import Decimal, ROUND_UP, ROUND_DOWN

print("Let's calculate City/Highway MPG!")
print("")

#gathering input from user for miles, gallons, and city percentage driving
while True:
  try:
    distance = float(input("How many miles did you travel? "))
  except ValueError:
    continue
  else:
    if distance <= 0:
      continue
    break
while True:
  try:
    gallons = float(input("How many gallons did you use? "))
  except ValueError:
    continue
  else:
    if gallons <= 0:
      continue
    break
while True:
  try:
    city = float(input("What percentage of city driving did you do? "))
  except ValueError:
    continue
  else:
    if city <= 0:
      continue
    break
print("")

#calculating highway percentage, overall mpg, city mpg, and highway mpg and rounding them
mpg = distance / gallons
smpg = Decimal(str(mpg)).quantize(Decimal('.1'))
highway = 100.0 - city

city100 = 0.857 * mpg
highway100 = mpg / 0.807

scity100 = Decimal(str(city100)).quantize(Decimal('.1'), rounding=ROUND_UP)
shighway100 = Decimal(str(highway100)).quantize(Decimal('.1'), rounding=ROUND_DOWN)

#printing current mpg, and city and highway percentage
print("Your mpg is: " + str(smpg))
print("You drove: " + str(city) + "% City/" + str(highway) + "% Highway")
print("")

#printing mpg if user drives 100% city or 100% highway
print("If you drove 100% City, your mpg would be: " + str(scity100))
print("If you drove 100% Highway, your mpg would be: " + str(shighway100))
