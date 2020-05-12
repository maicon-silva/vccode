# Crie um algoritmo que leia três números e mostre-os em ordem crescente.
# Criar função para ordem crescente
def ordem_crescente(a, b, c):
    def mostrar_ordem (maior, meio, menor):
        print(f"O número maior é {maior}.")
        print(f"O número do meio é {meio}.")
        print(f"O número menor é {menor}.")
    if a >= b and a >= c :
        maior = a
        if b >= c :
            meio = b
            menor = c
            mostrar_ordem(maior, meio, menor)
        elif c >= b:
            meio = c
            menor = b
            mostrar_ordem(maior, meio, menor)
    elif b >= a and b >= c :
        maior = b
        if a >= c :
            meio = a
            menor = c
            mostrar_ordem(maior, meio, menor)
        elif c >= a :
            meio = c
            menor = a
            mostrar_ordem(maior, meio, menor)
    elif c >= a and c >= b :
        maior = c
        if a >= b :
            meio = a
            menor = b
            mostrar_ordem(maior, meio, menor)
        elif b >= a :
            meio = b
            menor = a
            mostrar_ordem(maior, meio, menor)
# Inserir dados
a = float(input("Insira o número 1: "))
b = float(input("Insira o número 2: "))
c = float(input("Insira o número 3: "))
# Chamar a função.
ordem_crescente(a, b, c)
