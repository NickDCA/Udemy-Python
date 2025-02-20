numero_1 = input("Numero inteiro: ")

try:
    numero_1_inteiro = int(numero_1)
    if (numero_1_inteiro % 2) == 0:
        print(f"Numero {numero_1_inteiro} é PAR")
    else:
        print(f"Numero {numero_1_inteiro} é ÍMPAR")
except:
    print("Numero digitado é inválido")

hora = input("Hora: ")
hora_int = int(hora)

if hora_int >= 0 and hora_int < 12:
    print(f"Bom dia {hora}h")
elif hora_int >= 12 and hora_int < 18:
    print(f"Boa tarde {hora}h")
elif hora_int >= 18 and hora_int < 24:
    print(f"Boa noite {hora}h")
else:
    print("Horário inválido")


primeiro_nome = input("Primeiro nome: ")
tamanho_primeiro_nome = len(primeiro_nome)

if tamanho_primeiro_nome <= 4:
    print("Seu nome é curto")
elif tamanho_primeiro_nome > 4 and tamanho_primeiro_nome <= 6:
    print("Seu nome é normal")
elif tamanho_primeiro_nome > 6:
    print("Seu nome é grande")
