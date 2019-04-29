from decimal import Decimal
from math import pi

print("Let's calculate volume! Please choose one of the following shapes:\nbox, sphere, or pyramid.")
print("")

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
      volume = length * width * height
      print("")
      print("The volume of your box is: " + str(volume) + " units^3")
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
      volume = (4/3) * pi * (radius ** 3)
      svolume = Decimal(str(volume)).quantize(Decimal('.1'))
      print("")
      print("The volume of your sphere is: " + str(svolume) + " units^3")
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
      volume = (length * width * height) / 3
      svolume = Decimal(str(volume)).quantize(Decimal('.1'))
      print("")
      print("The volume of your pyramid is: " + str(svolume) + " units^3")
    else:
      continue
    break