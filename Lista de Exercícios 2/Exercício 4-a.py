# Crie um algoritmo que leia três números e mostre o maior número.
# 👼 Desconsidere a hipótese de números iguais
def maior_numero(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(f"O número {n1} é maior que os números {n2} e {n3}.")
    elif n2 > n3 :
        print(f"O número {n2} é maior que os números {n1} e {n3}.")
    else :
        print(f"O número {n3} é maior que os números {n1} e {n2}.")

n1 = float(input("Insira o número 1: "))
n2 = float(input("Insira o número 2: "))
n3 = float(input("Insira o número 3: "))

maior_numero(n1, n2, n3)
