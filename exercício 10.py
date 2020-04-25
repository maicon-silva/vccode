# Crie um algoritmo que calcule a área de um retângulo, sendo que os comprimentos da altura e da base são informados pelo usuário.
# A área do retângulo é calculada multiplicando-se a altura pela base.
# Variaveis dos lados e da area.
print("para calcular a área do retangulo precisamos da medida dos dois lados.")
altura = float(input("Insira o valor da altura do retangulo (lado 1): "))
base = float(input("Insira o valor da base do retangulo (lado 2): "))
area_retangulo = round((altura * base), 4)
# Mostra a área do retangulo.
print(f"A área do retangulo é {area_retangulo}")
