#importing decimal and rounding
from decimal import Decimal, ROUND_UP, ROUND_DOWN

print("Let's calculate city/highway mpg!")
print("")

#program loops until a float > 0 is entered
while True:
  try:
    mpg = float(input("What's your mpg? "))
  except ValueError:
    print("Not a number!")
    continue
  else:
    print ("")
    if mpg <= 0:
      print("Please enter a number > 0.")
      continue
      
#calculating, rounding, and printing 100% city and 100% highway mpg
    city100 = 0.857 * mpg
    highway100 = mpg / 0.807

    city100_round = (Decimal(str(city100)).quantize
                (Decimal('.1'), rounding=ROUND_UP))
    highway100_round = (Decimal(str(highway100)).quantize
                   (Decimal('.1'), rounding=ROUND_DOWN))

    print("If you drove 100% city, your mpg would be: {}."
          .format(city100_round))
    print("If you drove 100% highway, your mpg would be: {}."
          .format(highway100_round))
    break
