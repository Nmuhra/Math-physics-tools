import dis
from tkinter.tix import DisplayStyle

while True:
    variables = "distance, time, acceleration, velocity(f)"
    print("what is the missing variable?\n"+ variables)

    variable = input()

    def square_root(x):
        from math import sqrt
        print(sqrt(x))

    if variable == "distance":
       initial = int(input("initial velocity?\n"))
       acceleration = int(input("acceleration?\n"))
       time = int(input("time?\n"))
       final_velocity = initial+(acceleration*time)
       print(f"Final velocity is equal to {final_velocity} m/s^2")

    if variable == "time":
       initial = int(input("initial velocity?\n"))
       acceleration = int(input("acceleration?\n"))
       displacement = int(input("displacement?\n"))
       final_velocity = int(square_root(initial**+2*acceleration+displacement))
       print(f"Final velocity is equal to {final_velocity} m/s^2")

    if variable == "acceleration":
       final = int(input("final velocity?\n"))
       initial = int(input("initial velocity?\n"))
       time = int(input("time?\n"))
       displacement = ((final+initial)/2)*time
       print(f"Displacement will me equal to {displacement} m")

    if variable == "velocity(f)":
       initial = int(input("initial velocity?\n"))
       time = int(input("time?\n"))
       acceleration = int(input("acceleration?\n"))
       displacement = initial*time + 1/2*acceleration*time*time
       print(f"Displacement will be equal to {displacement} m")

    if variable == None:
       print("wrong input!")

    again = input("again? (yes/no): ").lower()
    
    if again !="yes":
        break
print("ok bye")
