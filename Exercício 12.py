# Crie um algoritmo que calcule a área de uma esfera, sendo que o comprimento do raio é informado pelo usuário. 
# A área da esfera é calculada multiplicando-se 4 vezes pi e o raio ao quadrado.
# Mostra as informações necessáras a tarefa
print("Para efetuarmos o cálculo da área da esfera, precisamos saber o valor do raio.")
# Importar a biblioteca matemática.
import math
# Variavel raio
raio_esfera = float(input("Insira o valor do raio da esfera: "))
area_esfera = 4 * math.pi * (raio_esfera**2)
area_esfera = round(area_esfera, 4)
print(f"A área da esfera é {area_esfera}.")