energy = input("missing: Mechanical, Kinetic, Potential\n").lower()
if energy =="mechanical":
  mass = int(input("mass: "))
  height = int(input("height: "))
  speed = int(input("speed: "))
  ME = round(mass*9.81*height + (1/2*mass**speed))
  print(f"Mechanical energy is equal to {ME} joules")
if energy =="kinetic":
  mass = int(input("mass: "))
  speed = int(input("speed: "))
  KE = round(1/2*mass**speed)
  print(f"Kinetic energy is equal to {KE} joules")
if energy =="potential":
  mass = int(input("mass: "))
  height = int(input("height: "))
  PE = round(mass*9.81*height)
  print(f"Potential energy is equal to {PE} joules")
