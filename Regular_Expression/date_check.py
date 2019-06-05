#date_check.py: Simple string date check

import re

#date check doesnt check if calender date exists
date_check1 = r"0[1-9]/0[1-9]/[1-9][0-9]"
date_check2 = r"0[1-9]/[1|2][0-9]/[1-9][0-9]"
date_check3 = r"0[1-9]/3[0-1]/[1-9][0-9]"
date_check4 = r"1[0-2]/0[1-9]/[1-9][0-9]"
date_check5 = r"1[0-2]/[1|2][0-9]/[1-9][0-9]"
date_check6 = r"1[0-2]/3[0-1]/[1-9][0-9]"

#loop continues until user inputs a valid date
while True:
  try:
    user_date = input("Input a valid date. ")
  except ValueError:
    continue
  else:
    if re.search(date_check1,user_date):
      print("Match!")
    elif re.search(date_check2,user_date):
      print("Match!")
    elif re.search(date_check3,user_date):
      print("Match!")
    elif re.search(date_check4,user_date):
      print("Match!")
    elif re.search(date_check5,user_date):
      print("Match!")
    elif re.search(date_check6,user_date):
      print("Match!")
    else:
      print("Invalid.")
      continue
    break
