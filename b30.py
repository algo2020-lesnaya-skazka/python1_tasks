table = 7
for i in range(1, 13) :
    print('What\' s' , i, 'x' , table, '?')
    guess = input()
    ans = i * table
    if int(guess) == ans :
        print('Correct !')
    else:
        print('No, it\' s', ans)
print('Finished')