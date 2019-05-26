#obd1_fuel_trim.py: Calculating fuel trim for my obd1 car

#printing to user to find vf value
print("""Hi! Let's figure out your cars Learned Value Fuel Trims! 
You will need a 10 megaohm+ input impedance voltmeter/
multimeter for this procedure. First, warm up your car 
to normal operating temperatures for 5-10 minutes. Then, 
rev your engine at approximately 2500 rpms for 2 minutes 
and let it idle afterwards. Now, open the diagnostic 
port in the engine bay. Using the multimeter on DCVolts 
at the lowest setting, probe your red positive wire to 
the Vf1 pin and probe your black negative wire to the 
E1 pin.""")
print("")

#values used to determine cutoff for each percentage,
#voltages, and whether car is running rich, normal, or lean
# < 0v = SUPER rich, -2x
# 0-1.24v = rich, -11 to -20
# 1.25-3.75v = normal, -10 to +10
# 3.76-5v = Lean, +11 to +30
# 5.01-6.25v = SUPER Lean, +20 to +30

# 0.125 = 1 %

#for loop  generator values for correct output
x_range = -124
y_range = 1
perc = -20
fuel_trim_perc = 0
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
        fuel_trim_perc = perc
      elif vf < -125:
        fuel_trim_perc = "-2x"
      elif vf > 6250:
        fuel_trim_perc = "3x"
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
print("Your car is running {},\nwith a {}% fuel trim."
      .format(fuel_trim,fuel_trim_perc))
