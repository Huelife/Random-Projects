#hr_check.py: Simple string hr check

import re

#checking 12 hr clock
hr_check1 = r"0[0-9]:[0-5][0-9][AM|PM]"
hr_check2 = r"1[0-2]:[0-5][0-9][AM|PM]"

#loop continues until user inputs a valid hour
while True:
  try:
    user_hr = input("Input a valid hour. ex. '04:22PM' ")
  except ValueError:
    continue
  else:
    if re.search(hr_check1,user_hr) or re.search(hr_check2,user_hr):
      print("Match!")
      break
    else:
      print("Invalid.")
      continue
