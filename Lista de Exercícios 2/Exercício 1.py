# Cria função para verificação se, positivo, negativo ou zero.
def verifica_numero(n):
    if n > 0:
        print(f"O número {n} é positivo!")
    elif n == 0:
        print(f"O número {n} é zero!")
    else:
        print(f"O número {n} é negativo!")

num = float(input("Insira um número para verificação: "))
verifica_numero(num)