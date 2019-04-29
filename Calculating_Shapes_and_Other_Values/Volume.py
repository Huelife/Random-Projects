#decimal and pi are imported for rounding and reasons and use of pi
from decimal import Decimal
from math import pi

print("Let's calculate volume! Please choose one of the following shapes:\nbox, sphere, or pyramid.")
print("")

#program loops until given shape is chosen and user inputs float value > 0
while True:
  try:
    shape = input("What shape is the object? ")
  except ValueError:
    continue
  else:
#user can input 'box' in 7 different formats
    if shape in ("box", "BOX", "bOx", "BoX", "boX", "Box", "BOx"):
      while True:
        try:
          length = float(input("What's the length of the box? "))
        except ValueError:
          continue
        else:
          if length <= 0:
            continue
          break
      while True:
        try:
          width = float(input("What's the width of the box? "))
        except ValueError:
          continue
        else:
          if width <= 0:
            continue
          break
      while True:
        try:
          height = float(input("What's the height of the box? "))
        except ValueError:
          continue
        else:
          if height <= 0:
            continue
          break
#volume of a box is calculated and printed using user input values: length, width, and height
      volume = length * width * height
      print("")
      print("The volume of your box is: " + str(volume) + " units^3")
#user can input 'sphere' in 7 different formats
    elif shape in ("sphere", "SPHERE", "Sphere", "sPHERE", "SPhere", "SPHere", "sPhere"):
      while True:
        try:
          radius = float(input("What's the radius? "))
        except ValueError:
          continue
        else:
          if radius <= 0:
            continue
          break
#volume of a sphere is calculated and printed using user input value: radius. Pi value and rounding used
      volume = (4/3) * pi * (radius ** 3)
      svolume = Decimal(str(volume)).quantize(Decimal('.1'))
      print("")
      print("The volume of your sphere is: " + str(svolume) + " units^3")
#user can input 'pyramid' in 7 different formats
    elif shape in ("pyramid", "PYRAMID", "Pyramid", "pYRAMID", "PYramid", "PYRamid", "pYramid"):
      while True:
        try:
          length = float(input("What's the length of the pyramid? "))
        except ValueError:
          continue
        else:
          if length <= 0:
            continue
          break
      while True:
        try:
          width = float(input("What's the width of the pyramid? "))
        except ValueError:
          continue
        else:
          if width <= 0:
            continue
          break
      while True:
        try:
          height = float(input("What's the height of the pyramid? "))
        except ValueError:
          continue
        else:
          if height <= 0:
            continue
          break
#volume of a pyramid is calculated and printed using user input value: length, width, and height. Rounding used
      volume = (length * width * height) / 3
      svolume = Decimal(str(volume)).quantize(Decimal('.1'))
      print("")
      print("The volume of your pyramid is: " + str(svolume) + " units^3")
    else:
      continue
    break
