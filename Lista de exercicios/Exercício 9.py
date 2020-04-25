# Crie um algoritmo que calcule a área de um quadrado, 
# sendo que o comprimento do lado é informado pelo usuário. 
# A área do quadrado é calculada elevando-se o lado ao quadrado.
# Variavel aresta e calculo para área.
aresta = float(input("Para calcular a área do quadrado digite o valor da aresta: "))
area_quadrado = round((aresta ** 2), 4)
# Mostra o resultado da área.
print(f"A área do quadrado é igual a {area_quadrado}.")