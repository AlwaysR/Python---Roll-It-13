while True:
    answer = input('Do you want to see the instructions? ').lower()
    if answer == 'yes' or answer == 'y' or answer == 'yea' or answer == 'yeah' or 'yes' in answer:
        print('Yes')
        break
    elif answer == 'no' or answer == 'n' or answer == 'nah' or 'no' in answer:
        print('No')
        break
    else:
        print('Please enter yes or no')
