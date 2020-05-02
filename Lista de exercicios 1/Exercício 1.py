# Problema
# Crie um algoritmo que receba, como entrada, o valor de três notas de um aluno - 
# com valor entre 0 e 10, e, em seguida, informe a média entre elas.

# Inicio e exlicação ao usuário.
print("Calcular média de 3 notas de alunos.")
# Variaveis de notas com os respectivos números.
n1 = float(input("Insira a nota 1: "))
n2 = float(input("Insira a nota 2: "))
n3 = float(input("Insira a nota 3: "))
# Calcular e arredondar a media para duas casas decimais.
media = round(((n1 + n2 + n3)/3),2)
# Imprimir média
print(f"A média do aluno é: {media}")