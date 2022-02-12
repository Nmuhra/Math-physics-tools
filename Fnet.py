while True:
    choice = input("fnet, mass, acceleration?: ").lower()

    if choice == "fnet":
        Mass= int(input("mass?\n"))
        acceleration= int(input("acceleration?\n"))
        Fnet = (Mass*acceleration)
        print(f"Fnet is equal to {Fnet}")

    if choice == "mass":
       fnet= int(input("fnet?\n"))
       acceleration= int(input("acceleration?\n"))
       mass = (fnet/acceleration)
       print(f"mass is equal to {mass}")

    if choice == "acceleration":
       fnet= int(input("fnet?\n"))
       mass= int(input("mass?\n"))
       acceleration = (fnet/mass)
       print(f"acceleration is equal to {acceleration}")
    
    again = input("again? (yes/no): ").lower()
    
    if again !="yes":
        break
print("ok bye")
