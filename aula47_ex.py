palavra = 'banana'

palavra_formada = ''
for letra in palavra:
    palavra_formada += '*'
print(palavra_formada)
tentativas = 0

while palavra_formada != palavra:
    letra_chute = input('Digite uma letra: ').lower()
    
    indice = 0
    for letra in palavra:
        if letra == letra_chute:
            palavra_formada = palavra_formada[:indice] + letra_chute + palavra_formada[indice + 1:]
        indice += 1
    
    tentativas += 1
    print(f'Palavra formada: {palavra_formada}')

print(f'Parabéns, você acertou com {tentativas} tentativas!')
            
            