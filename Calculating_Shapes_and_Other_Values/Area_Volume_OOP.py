from math import pi,sqrt
#-----------------------Area-Volume-Super-Class------------------
class Area_Volume:
  shape_name = ""
  def __init__(self,name):
    self.name = name
#-----------------------Area-Classes-----------------------------
class Circle_Area(Area_Volume):
  def __init__(self,name,radius,area):
    self.shape_name = "circle"
    self.radius = radius
    self.area = round((pi * (radius ** 2)),1)
    super().__init__(name)

class Square_Area(Area_Volume):
  def __init__(self,name,height,base,area):
    self.shape_name = "square"
    self.height = height
    self.base = base
    self.area = height * base
    super().__init__(name)

class Triangle_Area(Area_Volume):
  def __init__(self,name,height,base,area):
    self.shape_name = "triangle"
    self.height = height
    self.base = base
    self.area = (height * base) / 2
    super().__init__(name)
#-----------------------Volume-Classes----------------------------
class Sphere(Area_Volume):
  def __init__(self,name,radius,volume,surface_area):
    self.shape_name = "sphere"
    self.radius = radius
    self.volume = round(((4/3) * pi * (radius ** 3)),1)
    self.surface_area = round(((4 * pi) * (radius ** 2)),1)
    super().__init__(name)

class Box(Area_Volume):
  def __init__(self,name,length,width,height,volume,surface_area):
    self.shape_name = "box"
    self.length = length
    self.width = width
    self.height = height
    self.volume = length * width * height
    self.surface_area = (2 * length * width) + (2 * width * height) + (2 * length * height)
    super().__init__(name)

class Pyramid(Area_Volume):
  def __init__(self,name,length,width,height,volume,surface_area):
    self.shape_name = "pyramid"
    self.length = length
    self.width = width
    self.height = height
    self.volume = round(((length * width * height) / 3),1)
    self.surface_area = round(((length * width) + (length * sqrt(((width / 2)**2) + (height**2))) + (width * sqrt(((length / 2)**2) + (height**2)))),1)
    super().__init__(name)
#-----------------------Shapes-Dict-------------------------------
shapes_dict = {
  "circle": Circle_Area,
  "square": Square_Area,
  "triangle": Triangle_Area,
  "sphere": Sphere,
  "box": Box,
  "pyramid": Pyramid
}
#-----------------------while loop continues until user chooses an option
while True:
  try:
    user_area_volume = input("Do you want to find 'area', 'volume', or 'surface area'? ").lower()
  except ValueError:
    continue
  else:
#-----------------------while loop for area----------------------    
    if user_area_volume == "area":
      while True:
        try:
          print("  circle\n  square\n  triangle")
          user_shape = input("Please choose a shape. ").lower()
        except ValueError:
          continue
        else:
          if user_shape in shapes_dict and user_shape == "circle":
            while True:
              try:
                radius = float(input("What's the radius? "))
              except ValueError:
                print("Please enter a number > 0.")
                continue
              else:
                if radius <= 0:
                  print("Please enter a number > 0.")
                  continue
                print("")
                print("Area: {} units^2".format(shapes_dict[user_shape]("",radius,"").area))
                print("")
                break
          elif user_shape in shapes_dict and user_shape == "square" or user_shape == "triangle":
            while True:
              try:
                height = float(input("What's the height? "))
              except ValueError:
                print("Please enter a number > 0.")
                continue
              else:
                if height <= 0:
                  print("Please enter a number > 0.")
                  continue
                while True:
                  try:
                    base = float(input("What's the base? "))
                  except ValueError:
                    print("Please enter a number > 0.")
                    continue
                  else:
                    if base <= 0:
                      print("Please enter a number > 0.")
                      continue 
                    print("")
                    print("Area: {} units^2".format(shapes_dict[user_shape]("",height,base,"").area))
                    print("")
                    break
                break
          break
#-----------------------while loop for volume--------------------
    elif user_area_volume == "volume" or user_area_volume == "surface area":
      while True:
        try:
          print("  sphere\n  box\n  pyramid")
          user_shape = input("Please choose a shape. ").lower()
        except ValueError:
          continue
        else:
          if user_shape in shapes_dict and user_shape == "sphere":
            while True:
              try:
                radius = float(input("What's the radius? "))
              except ValueError:
                print("Please enter a number > 0.")
                continue
              else:
                if radius <= 0:
                  print("Please enter a number > 0.")
                  continue
                elif user_area_volume == "volume":
                  print("")
                  print("Volume: {} units^3".format(shapes_dict[user_shape]("",radius,"","").volume))
                  print("")
                elif user_area_volume == "surface area":
                  print("")
                  print("Surface Area: {} units^2".format(shapes_dict[user_shape]("",radius,"","").surface_area))
                  print("")
                break
          elif user_shape in shapes_dict and user_shape == "box" or user_shape == "pyramid":
            while True:
              try:
                length = float(input("What's the length? "))
              except ValueError:
                print("Please enter a number > 0.")
                continue
              else:
                if length <= 0:
                  print("Please enter a number > 0.")
                  continue
                while True:
                  try:
                    width = float(input("What's the width? "))
                  except ValueError:
                    print("Please enter a number > 0.")
                    continue
                  else:
                    if width <= 0:
                      print("Please enter a number > 0.")
                      continue
                    while True:
                      try:
                        height = float(input("What's the height? "))
                      except ValueError:
                        print("Please enter a number > 0.")
                        continue
                      else:
                        if height <=0:
                          print("Please enter a number > 0.")
                          continue
                        elif user_area_volume == "volume":
                          print("")
                          print("Volume: {} units^3".format(shapes_dict[user_shape]("",length,width,height,"","").volume))
                          print("")
                        elif user_area_volume == "surface area":
                          print("")
                          print("Surface Area: {} units^2".format(shapes_dict[user_shape]("",length,width,height,"","").surface_area))
                          print("")
                        break
                    break
                break
          break
    break
