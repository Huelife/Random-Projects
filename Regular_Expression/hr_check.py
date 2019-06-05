#hr_check.py: Simple string hr check

import re

hr_check = r""

#loop continues until user inputs a valid hour
while True:
  try:
    user_hr = input("Input a valid hour. ex. '04:22PM' ")
  except ValueError:
    continue
  else:
    if re.search(hr_check,user_hr):
      print("Match!")
      break
    else:
      print("Invalid.")
      continue
