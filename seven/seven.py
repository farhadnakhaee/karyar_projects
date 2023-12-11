def correct_answer(num1, num2, num3, num4):
  '''function that give answers of game'''
  operations = ["+", "-", "*", "/"]
  for op1 in operations:
    for op2 in operations:
      for op3 in operations:
        if eval(f"{num1} {op1} {num2} {op2} {num3} {op3} {num4}") == 7:
          print(f"\n{num1} {op1} {num2} {op2} {num3} {op3} {num4} = 7\n")

def seven(num1, num2, num3, num4):

  print(f'\n{num1} __ {num2} __ {num3} __ {num4} = 7\n')

  user_ans = 1
  while user_ans != 7:
    op1 = input('Enter -first- operator: ( + , - , * , / ) ')
    op2 = input('Enter -second- operator: ( + , - , * , / ) ')
    op3 = input('Enter -third- operator: ( + , - , * , / ) ')
    user_ans = eval(f'{num1} {op1} {num2} {op2} {num3} {op3} {num4}')

    if user_ans == 7:
      print(f'\n{num1} {op1} {num2} {op2} {num3} {op3} {num4} = 7\n')
      print('Thats Right')
      
    else:
      print('\nTry again!')
      h = input('\nDo you want to see answer? (y/n)')
      if h == 'y':
        correct_answer(num1, num2, num3, num4)
        break

name = input('Hello my friend, Welcome to SEVEN.\n\t Whats your name? ')
print(f'Ok, lets play {name.upper()}\n')
print('\n1. START\n2. How to play?\n3. About me\n4. Exit\n')
answer = input('please enter a number. (1, 2, 3 or 4)')

while True:
  if answer == '1':
    seven(7, 2, 3, 5)
    cont = input('continue? (y/n)')
    if cont == 'y':
      print('.'*15)
      seven(5, 6, 9, 1)
      cont = input('continue? (y/n)')
      if cont == 'y':
        print('.'*15)
        seven(7, 4, 8, 2)
        print('.'*15)
        print('End Game\nyou are smart! ')

  elif answer == '2':
    print(
      '\nAll you have to do is put the four main operations of multiplication'
      '\n,division, addition and subtraction in their correct order,\n'
      'so that the result is 7.'
      )

  elif answer == '3':
    print('\nIm FARHAD and glad you chose SEVEN.')

  else:
    print('\nBye\n')
    break
  print('\n1. START\n2. How to play?\n3. About me\n4. Exit\n')
  answer = input('please enter a number. (1, 2, 3 or 4)')