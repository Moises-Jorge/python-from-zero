from random import randint

pc_num = randint(1, 20)
counter = 1

while counter <= 5:
    user_num = int(input(f'Attempt {counter}/5 - Guess the number (1-20): '))
    if user_num < 1 or user_num > 20:
        print('Number outside the possible range. Try another number between 1 and 20')
        continue
    elif user_num < pc_num:
        print('Your guess is smaller than the secret number!')
    elif user_num > pc_num:
        print('Your guess is bigger than the secret number!')
    else:
        print(f"You won in {counter} {'attempts' if counter > 1 else 'attempt'}!")
        break
    counter += 1
if counter > 5:
    print(f'You lost. The number the computer chose was: {pc_num}!')
