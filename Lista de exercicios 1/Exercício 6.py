# Crie um algoritmo para calcular a média de duas notas digitadas pelo usuário, sendo que a segunda nota tem peso dois.
print("Aqui voce pode calcular a média de duas notas, sendo que a segunta tem peso 2.")
# Variaveis das notas.
n1 = float(input("Insira o valor da nota 1: "))
n2 = float(input("Insira o valor da nota 2: "))
# Calcula a média e mostra o resultado.
media = round(((n1+n2)/(1+2)),2)
print(f"A média das duas notas é {media}.")