# let's do trigonometry
# A^2 + B^2 = C^2

from cmath import sqrt


name= input("First give us your name please?\n")

print("Hi " +name + " let's do some trig together X>")

sides = "hypotenuse, opposite, adjacent"

unites=  "CM, M, Feet, KM"

print("what is your unit of measurment?\n "+ unites)

unit = input()

print("which side are you missing?\n "+ sides)

side = input()

if side == "hypotenuse":
    opposite=  int(input("opposite?\n"))
    adjacent=  int(input("adjacent?\n"))
    hypotenuse= sqrt(opposite**2 + adjacent**2)
    print(f"the Hypotenuse will be equal to {hypotenuse} {unit}")



