from decimal import Decimal, ROUND_UP

print("Hi! Let's figure out your candle's burn rate!\nFirst, weigh your candle before your burn it.")
print("")

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

while True:
  try:
    time = int(input("How man minutes was your candle burning for?"))
  except ValueError:
    continue
  else:
    if time <= 0:
      continue
    break

while True:
  try:
    fweight = float(input("How much does your candle weigh now?"))
  except ValueError:
    continue
  else:
    if fweight < 0:
      continue
    break

print("")
tweight = (iweight - fweight)
rate = tweight / time
srate = Decimal(str(rate)).quantize(Decimal('.01'), rounding=ROUND_UP)
ttime = iweight / float(srate)
hours = ttime / 60.0
shours = Decimal(str(hours)).quantize(Decimal('.01'), rounding=ROUND_UP)

print("Ok! Your candle burns at a rate of about: " + str(srate) + " grams/minute")
print("Your candle should be able to burn for approximately: " + str(shours) + " hours")