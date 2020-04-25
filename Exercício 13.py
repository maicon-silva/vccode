# Crie um algoritmo que calcule o volume de uma caixa d’água cilíndrica, 
# sendo que os comprimentos do raio e a altura são informados pelo usuário. 
# O volume é calculado multiplicando-se pi, o raio ao quadrado e a altura.
# Mostra ao usuário os valores necessários.
print("Para fazer-mos o cálculo da área da caixa d'água cilindrica são necessários os valores do raio e a altura.")
# Importar o módulo de funções matemáticas.
import math
# Variáveis de raio e altura da caixa.
raio_caixa = float(input("Insira o valor do raio da caixa: "))
altura_caixa = float(input("Insira o valor da altura da caixa: "))
area_caixa = math.pi * (raio_caixa**2) * altura_caixa
area_caixa = round(area_caixa, 4)
print(f"O valor da área da caixa d'água é {area_caixa}.")