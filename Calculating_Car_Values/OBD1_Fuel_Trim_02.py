#printing to user to find Vfi value
print("""Hi! Let's figure out your cars Learned Value Fuel Trims! 
You will need a 10 megaohm+ input impedance voltmeter/
multimeter for this procedure. First, warm up your car 
to normal operating temperatures for 5-10 minutes. Then, 
rev your engine at approximately 2500 rpms for 2 minutes 
and let it idle afterwards. Now, open the diagnostic 
port in the engine bay on the passenger side. Using the 
multimeter on DCVolts at the lowest setting, probe 
your red positive wire to the Vf1 pin and probe your 
black negative wire to the E1 pin.""")
print("")

#values used to determine cutoff for each percentage, voltages, and whether car is running rich, normal, or lean
# 0-1.24v = rich, -11 to -20
# 1.25-3.75v = normal, -10 to +10
# 3.76-5v = Lean, +11 to +20

# 0.125 = 1 %

# 0.000 = -20
# 0.125 = -19
# 0.250 = -18
# 0.375 = -17
# 0.500 = -16
# 0.625 = -15
# 0.750 = -14
# 0.875 = -13
# 1.000 = -12
# 1.125 = -11

# 1.250 = -10
# 1.375 = -9
# 1.500 = -8
# 1.625 = -7
# 1.750 = -6
# 1.875 = -5
# 2.000 = -4
# 2.125 = -3
# 2.250 = -2
# 2.375 = -1
# 2.500 = 0
# 2.625 = +1
# 2.750 = +2
# 2.875 = +3
# 3.000 = +4
# 3.125 = +5
# 3.250 = +6
# 3.375 = +7
# 3.500 = +8
# 3.625 = +9
# 3.750 = +10

# 3.875 = +11
# 4.000 = +12
# 4.125 = +13
# 4.250 = +14
# 4.375 = +15
# 4.500 = +16
# 4.625 = +17
# 4.750 = +18
# 4.875 = +19
# 5.000 = +20

#program loops until a float > 0 from user is obtained
while True:
  try:
    vf = float(input("What is your voltage reading? "))
  except ValueError:
    print("Not a number!")
    print("")
    continue
  else:
    if (vf < 0.000):
      print("Please enter a positive value.")
      print("")
      continue
#positive voltage values are from 0-5 and give specific strings, anything over 5 just displays a generic string
#voltage values are in increments of 0.125 and strings from -20 to + 20
    elif (vf >= 0.000 and vf < 1.250):
      f = "rich"
      if (vf == 0.000):
        p = "-20"
      elif (vf > 0.000 and vf <= 0.125):
        p = "-19"
      elif (vf > 0.125 and vf <= 0.250):
        p = "-18"
      elif (vf > 0.250 and vf <= 0.375):
        p = "-17"
      elif (vf > 0.375 and vf <= 0.500):
        p = "-16"
      elif (vf > 0.500 and vf <= 0.625):
        p = "-15"
      elif (vf > 0.625 and vf <= 0.750):
        p = "-14"
      elif (vf > 0.750 and vf <= 0.875):
        p = "-13"
      elif (vf > 0.875 and vf <= 1.000):
        p = "-12"
      elif (vf > 1.000 and vf <= 1.125):
        p = "-11"
      else:
        continue
      break
    elif (vf >= 1.250 and vf <= 3.750):
      f = "normal"
      if (vf > 1.125 and vf <= 1.250):
        p = "-10"
      elif (vf > 1.250 and vf <= 1.375):
        p = "-9"
      elif (vf > 1.375 and vf <= 1.500):
        p = "-8"
      elif (vf > 1.500 and vf <= 1.625):
        p = "-7"
      elif (vf > 1.625 and vf <= 1.750):
        p = "-6"
      elif (vf > 1.750 and vf <= 1.875):
        p = "-5"
      elif (vf > 1.875 and vf <= 2.000):
        p = "-4"
      elif (vf > 2.000 and vf <= 2.125):
        p = "-3"
      elif (vf > 2.125 and vf <= 2.250):
        p = "-2"
      elif (vf > 2.250 and vf <= 2.375):
        p = "-1"
      elif (vf > 2.375 and vf <= 2.500):
        p = "0"
      elif (vf > 2.500 and vf <= 2.625):
        p = "+1"
      elif (vf > 2.625 and vf <= 2.750):
        p = "+2"
      elif (vf > 2.750 and vf <= 2.875):
        p = "+3"
      elif (vf > 2.875 and vf <= 3.000):
        p = "+4"
      elif (vf > 3.000 and vf <= 3.125):
        p = "+5"
      elif (vf > 3.125 and vf <= 3.250):
        p = "+6"
      elif (vf > 3.250 and vf <= 3.375):
        p = "+7"
      elif (vf > 3.375 and vf <= 3.500):
        p = "+8"
      elif (vf > 3.500 and vf <= 3.625):
        p = "+9"
      elif (vf > 3.625 and vf <= 3.750):
        p = "+10"
      else:
        continue
      break
    elif (vf > 3.750 and vf <= 5.000):
      f = "lean"
      if (vf > 3.750 and vf <= 3.875):
        p = "+11"
      elif (vf > 3.875 and vf <= 4.000):
        p = "+12"
      elif (vf > 4.000 and vf <= 4.125):
        p = "+13"
      elif (vf > 4.125 and vf <= 4.250):
        p = "+14"
      elif (vf > 4.250 and vf <= 4.375):
        p = "+15"
      elif (vf > 4.375 and vf <= 4.500):
        p = "+16"
      elif (vf > 4.500 and vf <= 4.625):
        p = "+17"
      elif (vf > 4.625 and vf <= 4.750):
        p = "+18"
      elif (vf > 4.750 and vf <= 4.875):
        p = "+19"
      elif (vf > 4.875 and vf <= 5.000):
        p = "+20"
      else:
        continue
      break
    elif (vf > 5.000):
      f = "SUPER LEAN"
      p = "+2x value, out of range"
      break
    else:
      continue
#printed results
print("")
print("Based on your input, your car is running " + f + ",\nwith a " + p + "% fuel trim.")
