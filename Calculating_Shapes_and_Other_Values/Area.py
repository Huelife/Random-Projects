#importing decimal and math, decimal for rounding and math for pi
from decimal import Decimal
from math import pi

print("Let's calculate area!\nPlease choose one of the following shapes:\nbox, sphere, or pyramid.")
print("")

#while loop continues until a given shape is chosen and a value > 0 is used
while True:
  try:
    shape = input("What shape is the object? ")
  except ValueError:
    continue
  else:
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
#formula for area of a box
      area = (2*(height * width)) + (2*(height * length)) + (2*(width * length))
      print("")
      print("The area of your box is: " + str(area) + " units^2")
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
#formula for area of a sphere
      area = 4 * pi * (radius ** 2)
      sarea = Decimal(str(area)).quantize(Decimal('.1'))
      print("")
      print("The area of your sphere is: " + str(sarea) + " units^2")
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
#formula for area of a pyramid
      area = length * width + (length % (((width / 2)*(width / 2)) + (height*height))) + (width % (((length / 2)*(length / 2)) + (height*height)))
      sarea = Decimal(str(area)).quantize(Decimal('.1'))
      print("")
      print("The area of your pyramid is: " + str(sarea) + " units^2")
    else:
      continue
    break
