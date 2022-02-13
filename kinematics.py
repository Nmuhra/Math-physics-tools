variables = "distance, time, acceleration, velocity(f)"

print("what is the missing variable?\n"+ variables)

variable = input()

SolveD = "final, initial, acceleration, time : "

if variable == "distance":
    choice = input("solve for?\n" +SolveD)
    if choice == "final":
        initial = int(input("initial?\n"))
        acceleration = int(input("acceleration?\n"))
        time = int(input("time\n"))
        final_velocity = initial+(acceleration*time)
        print(f"final velocity is {final_velocity} m/s^2")
        


