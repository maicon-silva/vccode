# Crie um algoritmo que leia um caractere e informe se o mesmo é uma vogal ou não.
# Definir função de verificação para de vogal.
def verifica_vogal(v):
    v = l.casefold()
    if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u' :
        print(f"A letra {v} é vogal.")
    else:
        print(f"A letra {v} é consoante.")
# Fala o que o algorito faz.
print("Algoritmo para verificação de vogal.")
# Inserir letra
l = input("Insira a letra para verificação: ")
# Chamar função
verifica_vogal(l)