while True:
    num_1 = int(input('N1: '))
    num_2 = int(input('N2: '))
    operador = input('[+][-][*][/]')
    res = 0

    if operador == '+':
        res = num_1 + num_2
    elif operador == '-':
        res = num_1 - num_2
    elif operador == '*':
        res = num_1 * num_2
    elif operador == '/':
        res = num_1 / num_2
    else:
        print('Operador inválido! Tente novamente')

    print(f'Resultado = {res}')

    sair = input('Deseja [s]air? ').lower().startswith('s')
    if sair is True:
        print('Saindo...')
        break