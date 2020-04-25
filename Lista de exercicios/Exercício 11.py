# Crie um algoritmo que calcule a área de um círculo, sendo que o comprimento do raio é informado pelo usuário. 
# A área do círculo é calculada multiplicando-se pi e o raio ao quadrado.
# importa a bibliotea matematica.
import math
# Informa o que é necessário para os calculos.
print("Para calcular a área do círculo vamos precisar do valor do raio.")
# Variavel para o raio.
raio = float(input("Insira o valor do raio do círculo: "))
# Cria variável de calculo da área do circulo e limita a 4 casas decimais.
area_circulo = raio * math.pi
area_circulo = round(area_circulo,4)
# Mostra o resultado.
print(f"A área do circulo é {area_circulo}.")