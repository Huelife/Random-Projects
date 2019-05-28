#creating Weapon_stats class for attributes
class WeaponStats:
  def __init__(self,Strength,Agility,Speed,Defence,Vitality,Resistance,
               Piercing,Range):
    self.Strength = Strength
    self.Agility = Agility
    self.Speed = Speed
    self.Defence = Defence
    self.Vitality = Vitality
    self.Resistance = Resistance
    self.Piercing = Piercing
    self.Range = Range

#stat values for items in weapon_list
legendary_sword = WeaponStats("+100","+50","+50",0,0,0,0,0)
legendary_shield = WeaponStats(0,0,0,"+200","+200","+200",0,0)
legendary_gun = WeaponStats(0,"+100","+200",0,0,0,"+100",0)
legendary_bow = WeaponStats(0,"+200","+200",0,0,0,0,"+100")
legendary_axe = WeaponStats("+200","+25",0,0,"+50",0,0,0)

print("Choose your weapon!")
print("")

#declaring weapon_list dict and printing the item names
weapon_list = {
  "Legendary Sword":legendary_sword,
  "Legendary Shield":legendary_shield,
  "Legendary Gun":legendary_gun,
  "Legendary Bow":legendary_bow,
  "Legendary Axe":legendary_axe
}

for key, value in weapon_list.items():
  print(key)
print("")

#while loop continues until user inputs 'Quit'
while True:
  try:
    weapon = input("Choose a weapon to show its attributes, "
                   "otherwise, enter 'Quit' to leave. ")
  except ValueError:
    continue
  else:
    if weapon == "Quit":
      break
    elif weapon in weapon_list:
      print("")
      print("="*len(weapon))
      print(weapon)
      print("="*len(weapon))
      print("".join("%s: %s\n" % stats for stats in vars(weapon_list[weapon])
            .items()))
    else:
      print("{} is an invalid option.".format(weapon))
    continue
