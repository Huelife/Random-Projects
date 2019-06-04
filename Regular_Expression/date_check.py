#date_check.py: Simple string date check

import re

#date check doesnt check if calender date exists
date_check = r"[1-12]/[1-31]/[19-99]"

#loop continues until user inputs a valid date
while True:
  try:
    user_date = input("Input a valid date. ")
  except ValueError:
    continue
  else:
    if re.search(date_check,user_date):
      print("Match!")
      break
    else:
      print("Invalid.")
      continue
