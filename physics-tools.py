# let's go, I am going to make a program that can help with simple physics problem

print("DO you keep on forgetting your physics formulas, well.. I do, that's why I made this program that helps me remember all the formulas and I am sharing it with you.")

name= input("First give us your name please?\n")

print("Thank you for joining us"+ name )

formulas = "Mass-Formula, Displacement-Formula, Frequency-Formula, Weight-Formula, Acceleration-Formula"

print(name + ", which formula do you want to use for your problem?\n "+ formulas)

form = input()

if form == "Mass-Formula":
 
    print(f"the {form} states that m=F/a, where F= force, and a= acceleration")

if form == "Displacement-Formula":
 
    print(f"the {form} states that s = Vi*t + 1/2(a*t^2), where Vi= initial velocity, t= time, and a= acceleration")

if form == "Frequency-Formula":
 
    print(f"the {form} states that f= 1/T, where f= frequency, and T= period")

if form == "Weight-Formula":
 
    print(f"the {form} states that W= m*g, where m= Mass, and g= acceleration of gravity")

if form == "Acceleration-Formula":
 
    print(f"the {form} states that a= (Vf-Vi)/t, where Vf= final velocity, Vi= initial velocity, and t= time")



 






