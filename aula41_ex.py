frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'


letra_maior_frequencia = frase[0].lower()
i = 0
while i < len(frase):
    letra_atual = frase[i].lower()

    if letra_atual == ' ':
        print('Pulando [espaço]...')
        i += 1
        continue

    frequencia_letra_atual = frase.count(letra_atual)
    print(f'Letra atual: {letra_atual} | Frequência: {frequencia_letra_atual}')
    
    if frequencia_letra_atual > frase.count(letra_maior_frequencia):
        letra_maior_frequencia = letra_atual
        print(f'Letra mais frequente atualizada: {letra_maior_frequencia}')
    
    i += 1

print(f'Letra que apareceu mais vezes: [{letra_maior_frequencia}]')
    
