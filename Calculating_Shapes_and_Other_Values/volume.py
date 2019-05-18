#decimal and pi are imported for rounding and reasons and use of pi
from decimal import Decimal
from math import pi

print("Let's calculate volume! Please choose one of the following shapes:\n'box', 'sphere', or 'pyramid'.")
print("")

box_tuple = ("box", "BOX", "bOx", "BoX", "boX", "Box", "BOx")
pyramid_tuple = ("pyramid", "PYRAMID", "Pyramid", "pYRAMID", "PYramid", "PYRamid", "pYramid")

#program loops until given shape is chosen and user inputs float value > 0
while True:
  try:
    shape = input("What shape is the object? ")
  except ValueError:
    continue
  else:
    
#user can input 'box' in 7 different formats
    if shape in box_tuple or shape in pyramid_tuple:
      while True:
        try:
          length = float(input("What's the length of the {}? ".format(shape)))
        except ValueError:
          print("Not a number!")
          continue
        else:
          if length <= 0:
            print("Please input a value > 0.")
            continue
          break
      while True:
        try:
          width = float(input("What's the width of the {}? ".format(shape)))
        except ValueError:
          print("Not a number!")
          continue
        else:
          if width <= 0:
            print("Please input a value > 0.")
            continue
          break
      while True:
        try:
          height = float(input("What's the height of the {}? ".format(shape)))
        except ValueError:
          print("Not a number!")
          continue
        else:
          if height <= 0:
            print("Please input a value > 0.")
            continue
          break
          
#volume of a box is calculated and printed using user input values: length, width, and height
      if shape in box_tuple:
        volume = length * width * height
        print("")
        print("The volume of your box is: " + str(volume) + " units^3")
        
#volume of a pyramid is calculated and printed using user input value: length, width, and height. Rounding used to 0.1 of a decimal
      elif shape in pyramid_tuple:
        volume = (length * width * height) / 3
        svolume = Decimal(str(volume)).quantize(Decimal('.1'))
        print("")
        print("The volume of your pyramid is: " + str(svolume) + " units^3")
        
#user can input 'sphere' in 7 different formats
    elif shape in ("sphere", "SPHERE", "Sphere", "sPHERE", "SPhere", "SPHere", "sPhere"):
      while True:
        try:
          radius = float(input("What's the radius? "))
        except ValueError:
          print("Not a number!")
          continue
        else:
          if radius <= 0:
            print("Please input a value > 0.")
            continue
          break
          
#volume of a sphere is calculated and printed using user input value: radius. Pi value and rounding used to 0.1 of a decimal
      volume = (4/3) * pi * (radius ** 3)
      svolume = Decimal(str(volume)).quantize(Decimal('.1'))
    
      print("")
      print("The volume of your sphere is: " + str(svolume) + " units^3")
      
    else:
      print("{} is not a valid option.".format(shape))
      continue
    break