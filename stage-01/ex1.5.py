from random import randint

pc_num = randint(1, 20)
counter = 1
while counter <= 5:
    user_num = int(input('What number did the computer choose?: '))
    if user_num < pc_num:
        print('smaller')
    elif user_num > pc_num:
        print('bigger')
    else:
        print(f'You won in {counter} attempts')
        break
    counter += 1
