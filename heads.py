import random

def heads():
    user_input = input('Heads or Tails? \n')

    if 'head' in user_input.lower() and 'tail' in user_input.lower():
        print("It doesn't work like that...")
        exit()
    elif 'head' in user_input.lower() or user_input.lower() == 'h':
        print('Your pick: Heads')
    elif 'tail' in user_input.lower() or user_input.lower() == 't':
        print('Your pick: Tails')
    else:
        print("You didn't pick any!")

    pick = random.choice(['Tails', 'Heads'])
    cpu_input = str(pick)

    print('CPU pick: ', cpu_input)

    if user_input.lower() in cpu_input.lower():
        print('You guessed it!')
    else:
        print('Maybe next time :(')


heads()
