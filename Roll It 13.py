#Functions Here:

def yes_no(question):

    while True:

        """Takes yes no question and gets input"""
        
        answer = input(question).lower()
        if answer == 'yes' or answer == 'y' or answer == 'yea' or answer == 'yeah' or 'yes' in answer:
           return "yes"
        elif answer == 'no' or answer == 'n' or answer == 'nah' or 'no' in answer:
           return "no"
        else:
            print('Please enter yes or no')

def instructions():

    print("""
*** Instructions ***

Roll the dice and try to win!
""")

def integer_checker(minimun, message):
    while True:
        try:
            response = int(input(message))
            if response >= minimun:
                return response
            else:
                print(f"Please enter a number equal to or over {minimun}")
        except ValueError:
            print("Please enter a valid whole number.")

#Main Code Here:

wants_instructions = yes_no('Do you want instructions? ')

if wants_instructions == "yes":
    instructions()

game_goal = integer_checker(13, "What is the game goal? ")
print(game_goal)
