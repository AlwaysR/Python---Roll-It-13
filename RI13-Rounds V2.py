def initial_points(which_player):

    double = False

    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if which_player == "User" and roll_one == roll_two:
        double = True

    total = roll_one + roll_two

    print(f"{which_player}     - Roll 1: {roll_one} \t| Roll 2: {roll_two}  \t| Total: {total} ")

    return total, double

import random

user_points = 0
comp_points = 0

initial_user = initial_points("User")
initial_comp = initial_points("Comp")

user_points = initial_user[0]
comp_points = initial_comp[0]

double_user = initial_user[1]

if double_user == True:
    print("Great news - if you win you get double points!")

first = "User"
second = "Computer"
p1_points = user_points
p2_points = comp_points

if user_points < comp_points:
    print("You start because your initial roll was less than the computer\n")

elif user_points == comp_points:
    print("The initial rolls were the same, the user starts!")

else:
    p1_points, p2_points = p2_points, p1_points
    first, second = second, first

while p1_points < 13 and p2_points < 13:
    print()
    input("Press <enter> to continue this round.\n")

    p1_roll = random.randint(1, 6)
    p1_points = p1_points + p1_roll

    print(f"{first}: Rolled a {p1_roll} - has {p1_points} points.")

    if p1_points >= 13:
        break

    p2_roll = random.randint(1, 6)
    p2_points = p2_points + p2_roll

    print(f"{second}: Rolled a {p2_roll} - has {p2_points} points.")
    
    if p1_points >= 13:
        break

    print(f"{first}: {p1_points} | {second} {p2_points}")

print("End Of Round")
