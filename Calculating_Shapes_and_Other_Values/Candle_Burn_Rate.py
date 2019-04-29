#importing decimal and rounding to round up
from decimal import Decimal, ROUND_UP

print("Hi! Let's figure out your candle's burn rate!\nFirst, weigh your candle before your burn it.")
print("")

#while loop continues until a value >= 0 is chosen
while True:
  try:
    iweight = float(input("What's the weight in grams?"))
  except ValueError:
    continue
  else:
    if iweight <= 0:
      continue
    break

print("")
print("Ok! Now use your candle for at least 30 minutes while timing it.")
print("")

#while loop continues until a value >= 0 is chosen
while True:
  try:
    time = int(input("How man minutes was your candle burning for?"))
  except ValueError:
    continue
  else:
    if time <= 0:
      continue
    break

#while loop continues until a value > 0 is chosen
while True:
  try:
    fweight = float(input("How much does your candle weigh now?"))
  except ValueError:
    continue
  else:
    if fweight < 0:
      continue
    break

#all values obtained by user input is calculated, rounded up, and printed for user
#initial weight, time for candle burn, and final weight are from user input
#total weight difference, rate of burn, total time in minutes, and total time in hours calculated from user input
#these actions are done outside of any of the previous while loops
print("")
tweight = (iweight - fweight)
rate = tweight / time
srate = Decimal(str(rate)).quantize(Decimal('.01'), rounding=ROUND_UP)
ttime = iweight / float(srate)
hours = ttime / 60.0
shours = Decimal(str(hours)).quantize(Decimal('.01'), rounding=ROUND_UP)

#rate is in grams/mins and how many total hours the candle can burn for
print("Ok! Your candle burns at a rate of about: " + str(srate) + " grams/minute")
print("Your candle should be able to burn for approximately: " + str(shours) + " hours")
