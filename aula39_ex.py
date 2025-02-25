nome = "Nicolas David"
tamanho_nome = len(nome)

nova_string = ""
i = 0
while i < tamanho_nome:
    nova_string += '*' + nome[i]
    i += 1
    print(nova_string)
    
