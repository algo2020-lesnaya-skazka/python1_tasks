from turtle import * 
def turtle_controller(do, val):
    do = do.upper()
    if do == 'F':
        forward(val)
    elif do == 'B':
        backward(val)
    elif do == 'R':
        right(val)
    elif do == 'L':
        left(val)
    elif do == 'U':
        punup()
    elif do == 'D':
        pendown()
    elif do == 'N':
        reset()
    else :
        print('Unrecorgnized command')
def string_artist(program):
    cmd_list = program.split('-')
    for command in cmd_list:
        cmd_len = len(command)
        if cmd_len == 0:
            continue
        cmd_type = command[0]
        num = 0
        if cmd_len > 1:
            num_string = command[1:]
            num = int(num_string)
        print(command, ':', cmd_type, num)
        turtle_controller(cmd_type, num)
string_artist('N-L90-F100-R45-F70-R90-F70-R45-F100-R90-F100')