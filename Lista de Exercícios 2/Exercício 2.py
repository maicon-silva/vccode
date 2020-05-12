#  Crie um algoritmo que leia um número e mostre se o mesmo é par ou ímpar.
num = int(input("Insira o número que deseja verificar: "))
if (num % 2) == 0:
    print(f"O número {num} é par!")
else:
    print(f"O número {num} é ímpar.")