#importing decimal and pi, decimal for rounding and pi for its value
from decimal import Decimal
from math import pi

print("Let's calculate surface area!\nPlease choose one of the following shapes:\n'box', 'sphere', or 'pyramid'.")
print("")

#possible inputs for box and pyramid
shape_box = ("box", "BOX", "bOx", "BoX", "boX", "Box", "BOx")
shape_pyramid = ("pyramid", "PYRAMID", "Pyramid", "pYRAMID", "PYramid", "PYRamid", "pYramid")

#while loop continues until a given shape is chosen and a float value > 0 is used
while True:
  try:
    shape = input("What shape is the object? ")
  except ValueError:
    continue
  else:
    
#user can input 'box' in 7 different formats and 'pyramid' in 7 different formats
    if shape in shape_box or shape in shape_pyramid:
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
          
#user input of height, width, and length used
#formula for area of a box is calulated and printed
        if shape in shape_box:
          area = (2*(height * width)) + (2*(height * length)) + (2*(width * length))
          print("")
          print("The surface area of your {} is: {} units^2".format(shape,area))
          
#user input of length, width, and height is used
#formula for area of a pyramid is calculated, rounded to 0.1 of a decimal, and printed
        elif shape in shape_pyramid:
          area = length * width + (length % (((width / 2)*(width / 2)) + (height*height))) + (width % (((length / 2)*(length / 2)) + (height*height)))
          sarea = Decimal(str(area)).quantize(Decimal('.1'))
          print("")
          print("The surface area of your {} is: {} units^2".format(shape,sarea))
          
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
          
#user input of radius is used
#formula for area of a sphere is calculated, rounded to 0.1 of a decimal and printed
      area = 4 * pi * (radius ** 2)
      sarea = Decimal(str(area)).quantize(Decimal('.1'))
      print("")
      print("The surface area of your sphere is: {} units^2".format(sarea))
    else:
      print("{} is not a valid input.".format(shape))
      continue
    break
