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
# < 0v = SUPER rich, -2x
# 0-1.24v = rich, -11 to -20
# 1.25-3.75v = normal, -10 to +10
# 3.76-5v = Lean, +11 to +30
# 5.01-6.25v = SUPER Lean, +20 to +30

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
# 5.125 = +21
# 5.250 = +22
# 5.375 = +23
# 5.500 = +24
# 5.625 = +25
# 5.750 = +26
# 5.875 = +27
# 6.000 = +28
# 6.125 = +29
# 6.250 = +30

x_range = -124
y_range = 1
percentage = -20
fuel_trim_percentage = 0
fuel_trim = ""
#program loops until user inputs a float value
while True:
  try:
    vf = float(input("What is your voltage reading? "))*1000
  except ValueError:
    print("Not a number!")
    continue
  else:
    for i in range(51):
      if vf in range(x_range,y_range):
        fuel_trim_percentage = percentage
      elif vf < -125:
        fuel_trim_percentage = "-2x"
      elif vf > 6250:
        fuel_trim_percentage = "3x"
      if vf < 0:
        fuel_trim = "SUPER RICH"
      elif vf in range(-1,1250):
        fuel_trim = "rich"
      elif vf in range(1249,3751):
        fuel_trim = "normal"
      elif vf in range(3750,5001):
        fuel_trim = "lean"
      elif vf > 5000:
        fuel_trim = "SUPER LEAN"
      percentage += 1
      x_range += 125
      y_range += 125      
    break
#printed results
print("")
print("Your car is running " + str(fuel_trim) + ",\nwith a " + str(fuel_trim_percentage) + "% fuel trim.")
