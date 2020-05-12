# Crie um algoritmo que leia dois números e mostre o maior número.
# Define a função para verificação do númeor maior e imprime qual é o maior, ou se são iguais.
def verificar_maior(n1, n2):
    if n1 > n2:
        print(f"O número {n1} é maior que o número {n2}.")
    elif n1 == n2:
        print("Os dois números são iguais.")
    else :
        print(f"O número {n2} é maior que o número {n1}.")

x = float(input("Insira o número 1: "))
y = float(input("Insira p número 2: "))

verificar_maior(x, y)