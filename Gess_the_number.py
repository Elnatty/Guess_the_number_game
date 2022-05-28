import random

def guess(x):
    random_number = random.randint(1, x)
    gess = 0
    tries = 4
    while tries > 0:
        tries -= 1
        gess = int(input(f'Guess a number between 1 and {x} >>> '))
        if gess < random_number:
            print(f'Sorry, too Low... {tries} tries left, be careful')
        elif gess > random_number:
            print(f'Sorry, too High... {tries} tries left, be careful')
        elif gess == random_number:
            print(f'Yay, Congrats.. u guessed {random_number} correctly after {tries} tries')
            raise SystemExit
    print(f'{tries} tries left... goodluck next time!')
    raise SystemExit
# guess(10)


def computer_gess(x):
    low = 1
    high = x
    feedback = ''
    tries = 4
    while tries > 0:
        tries -= 1
        gess = random.randint(low, high)
        feedback = input(f'Is {gess} too high (H), too low (L), or correct (C) >>> ').lower()
        if feedback == 'l':
            low = gess + 1
            print(f'Computer has {tries} tries left..')
        elif feedback == 'h':
            high = gess - 1
            print(f'Computer has {tries} tries left..')
    print(f'Congrats to Computer..., Won after {tries} tries')
#  computer_gess(10)

