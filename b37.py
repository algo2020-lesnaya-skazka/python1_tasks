def num_input(prompt) :
    typed = input(prompt)
    num = int(typed)
    return num
a = num_input('Enter a')
b = num_input('Enter b')
print('a + b =', a + b)