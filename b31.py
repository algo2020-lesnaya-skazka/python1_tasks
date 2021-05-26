from random import randint
a = randint(1, 10)
while True:
    print("угадай число")
    b = int(input())
    if b == a :
        print('угадал')
        print('конец')
        break
    else:
        print('не угадал, ещё раз')
