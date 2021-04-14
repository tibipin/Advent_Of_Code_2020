# Link to challenge: https://adventofcode.com/2020/day/8

import os

current_folder = f'{os.getcwd()}'

# Parsing the file

data = {i: {'sign': j.split()[1][0],
            'value': int(j.split()[1][1:]),
            'instruction': j.split()[0]}
        for i, j in enumerate(open(f'{current_folder}/input.txt', 'r').readlines())}

# Solving the puzzle

a = ['a']


def fuck_this(start=0, acc=0):

    if start not in a:
        a.append(start)
    else:
        return print(f'Pasul care se repeta este {start} si valoarea acc este {acc}')

    if data[start]['instruction'] == 'acc':
        if data[start]['sign'] == '+':
            acc += data[start]['value']
            start += 1
            fuck_this(start=start, acc=acc)
        else:
            acc -= data[start]['value']
            start += 1
            fuck_this(start=start, acc=acc)
    elif data[start]['instruction'] == 'jmp':
        if data[start]['sign'] == '+':
            start += data[start]['value']
        else:
            start -= data[start]['value']
        fuck_this(start=start, acc=acc)
    else:
        start += 1
        fuck_this(start=start, acc=acc)


fuck_this()