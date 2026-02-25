def initial_points(which_player):

    double = False

    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if which_player == "User" and roll_one == roll_two:
        double = True

    total = roll_one + roll_two

    print(f"{which_player}     - Roll 1: {roll_one} \t| Roll 2: {roll_two}  \t| Total: {total} ")

    return total, double

def make_statement(statement, decoration):

    ends = decoration * 3

    print(f'\n{ends} {statement} {ends}')

def yes_no(question):

    while True:

        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes/no")

def int_check():

    error = "Please enter an integer more than / equal to 13."

    while True:
        try:
            response = int(input("What is the game goal? "))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

def instructions():

    make_statement("Instructions", "*")

    print("Roll the dice and try to win")

import random

make_statement("Welcome to the Roll It 13 Game", "🍀")

game_history = []
comp_score = 0
user_score = 0
rounds_played = 0

want_instructions = yes_no("Do you want instructions? ")
if want_instructions == "yes":
    instructions()
print()
game_goal = int_check()

while comp_score < game_goal and user_score < game_goal:

    rounds_played += 1
    make_statement(f"Round {rounds_played}", "🎲")

    make_statement("Starting Rolls are:", "💎")

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

    #End Of Round

    user_points = p1_points
    comp_points = p2_points

    if first == "Computer":
        user_points, comp_points = comp_points, user_points

    if user_points > comp_points:
        winner = "User"
        loser = "Comp"
        comp_points = 0

    else:
        winner = "Computer"
        loser = "User"
        user_points = 0


    if winner == "User" and double_user == True:
        user_points = user_points * 2

    make_statement("Round Results", "💎")
    print(f"""
    User points: {user_points} | Computer points: {comp_points}
              The {winner} won! The {loser}'s points have been reset to zero."
    """)

    comp_score += comp_points
    user_score += user_points

    make_statement("Game Update", "💎")
    print(f'User Score: {user_score} | Computer Score {comp_score}')
    print()

    game_results = (f"Round {rounds_played}: User Points {user_points} |"
                    f"Computer Points {comp_points}, {winner} wins ({user_score} | {comp_score})")

    game_history.append(game_results)

    input("Press <enter> to continue the next round")

make_statement("Game Over", "👾")

print()
if user_score > comp_score:
    make_statement("The user won", "💎")

else:
    make_statement("The computer won", "💎")

    
print()
print("Game History")

for item in game_history:
    print(item)
