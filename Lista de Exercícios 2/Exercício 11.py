# Definir função para calcular a quantidade de pontos feita pelo robo, com base na distancia da cesta.
# A medida a ser inserida é em centimtros com restrições: 0 ≤ D ≤ 2000.
def pontos_distancia(centimetros):
    # Verificação das distancias e rtorno em pontos.
    if centimetros >= 0 and centimetros <= 800:
        print("1 ponto.")
    elif centimetros > 800 and centimetros <= 1400 :
        print("2 pontos.")
    elif centimetros > 1400 and centimetros <= 2000:
        print("3 pontos.")
    # Se o número estiver fora do intervalo retornar inválido.
    else:
        print("O valor inserido é inválido.")
# Inserir distancia.
d = int(input("Insira a distacia em centimetros: " ))
# Chamar função.
pontos_distancia(d)