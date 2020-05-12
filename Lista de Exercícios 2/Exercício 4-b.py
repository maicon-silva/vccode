# Crie um algoritmo que leia três números e mostre o maior número.
# 😈 Considere-a, para um problema mais difícil.
# Definir a função.
def maior_numero(n1, n2, n3):
    # Verificar e mostrar o maior.
    if n1 > n2 and n1 > n3:
        print(f"O número {n1} é maior.")
    elif n2 > n3 and n2 > n1:
        print(f"O número {n2} é maior.")
    elif n3 > n2 and n3 >n1 :
        print(f"O número {n3} é maior.")
    # Verificar e mostrar a igualdade.
    elif n1 == n2 and n1 == n3 :
        print(f"Os números 1, 2 e 3 são iguais.")
    elif n1 == n2 :
        print(f"Os números 1 e 2 são iguais.")
    elif n2 == n3 :
        print(f"Os números 2 e 3 são iguais.")
    elif n1 == n3 :
        print(f"Os números 1 e 3 são guais.")
# Inserir os dados.
n1 = float(input("Insira o número 1: "))
n2 = float(input("Insira o número 2: "))
n3 = float(input("Insira o número 3: "))
# Chamar a função.
maior_numero(n1, n2, n3)