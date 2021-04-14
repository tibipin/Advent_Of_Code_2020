input_data = {
    f.replace('bags', '').strip('\n').split('contain')[0].strip(' '):
        {
            f"{i.replace('bags', '').replace('bag', '').strip(' ').split(' ')[1]} "
            f"{i.replace('bags', '').replace('bag', '').strip(' ').split(' ')[2]}":
            int(i.replace('bags', '').replace('bag', '').strip(' ').split(' ')[0])
            for i in f.strip('\n').strip('.').split('contain ')[1].split(', ')
            if i != 'no other bags'
        }
    for f in open('input.txt', 'r').readlines()
    }

lista_magica = [1]


def fuck_this(bag):
    contor = len(lista_magica)-1
    if input_data[bag]:
        for k in input_data[bag]:
            lista_magica.append(lista_magica[contor]*input_data[bag][k])
            fuck_this(bag=k)
    else:
        contor -= 1


fuck_this('shiny gold')

print(f'The result is: {sum(lista_magica)-1}')

'Link to challenge: https://adventofcode.com/2020/day/7'