from random import randint
a = random
while True:
    print()
    if guess == 'stop' :
        break
    if guess == 'skip' :
        print('Skipping')
        continue
    ans = i * table
    if int(guess) == ans :
        print('Correct !')
    else:
        print('No, it\' s', ans)
print('Finished')