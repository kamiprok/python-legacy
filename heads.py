import random

user_input = input('Heads or Tails? \n')

if 'head' in user_input.lower():
  print('Your pick: Heads')
elif 'tail' in user_input.lower():
  print('Your pick: Tails')
else:
  print('problem')

pick = random.choice(['Tails', 'Heads'])
cpu_input = str(pick)

print('CPU pick: ', cpu_input)

if user_input.lower() in cpu_input.lower():
  print('You guessed it!')
else:
  print('Maybe next time :(')
