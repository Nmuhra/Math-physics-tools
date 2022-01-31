# let's go, I am going to make a program that can help with simple physics problem

print("Do you keep on forgetting your physics formulas, well.. I do, that's why I made this program that helps me remember all the formulas and I am sharing it with you.")

name= input("First give us your name please?\n")

print("Thank you for joining us"+ name )

formulas = "Mass-Formula, Displacement-Formula, Frequency-Formula, Weight-Formula, Acceleration-Formula"

print(name + ", which formula do you want to use for your problem?\n "+ formulas)

form = input()

if form == "Mass-Formula":
        force=  int(input("force?\n"))
        acceleration=  int(input("acceleration?\n"))
        Mass= round(force/acceleration, 2)
        print(f"mass will be equal to {Mass}g")

if form == "Displacement-Formula":
        velocity=  int(input("initial velocity?\n"))
        Time=  int(input("time?\n"))
        acceleration=  int(input("acceleration?\n"))
        Displacement= round((velocity*Time)+(1/2)*(acceleration**Time))
        print(f"Displacement will be equal to {Displacement}m")

if form == "Frequency-Formula":
    period=  int(input("Period?\n"))
    frequency= round(1/period, 2)
    print(f"frequency will be equal to {frequency}hz")

if form == "Weight-Formula":
    Mass=  int(input("mass?\n"))
    gravity=  int(input("gravitational acceleration?\n"))
    weight= round(Mass*gravity, 2)
    print(f"weight will be equal to {weight}N")

if form == "Acceleration-Formula":
    Velocity1=  int(input("final velocity?\n"))
    velocity2=  int(input("initial velocity?\n"))
    Time= int(input("Time?\n"))
    acceleration= round((Velocity1-velocity2)/Time, 2)
    print(f"acceleration will be equal to {acceleration}m/s^2")





