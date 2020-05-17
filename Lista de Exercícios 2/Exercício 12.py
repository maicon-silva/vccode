# (Python Brasil) Faça um Programa para um caixa eletrônico. 
# O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, 
# uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
# uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
# Contar notas de 1 real
def contar_notas_1(valor1):
    # Limitar quantias a serem contadas para a nota de um, para ser somente valores abaixo de 5.
    if valor1 >= 1 and valor1 < 5:
        #Criar Variavel e verificar quantidade de notas de 1 real a serem sacadas.
        notas_1 = valor1 // 1
        # Mostrar quantidade de notas de 1 real.
        print(f"{notas_1} de 1 real")
# Contar notas de 5 reais.
def contar_notas_5(valor5):
    # Limitar quantias a serem contadas como nota de 5, para ser somente valores abaixo de 9 reais.
    if valor5 >= 5 and valor5 < 10:
         #Criar Variavel e verificar quantidade de notas de 5 reais a serem sacadas.
        notas_5 = valor5 // 5
        # Mostrar quantidade de notas de 5 reais.
        print(f"{notas_5} de 5 reais")
        # Criar variável e calcular o resto que precisa ser calcula em notas de inferiores.
        resto_5 = valor5 % 5
        # Verificar variável e calcular a quantidade em notas de inferiores.
        if resto_5 < 5:
            # Chamar a função para calcular notas de 1 real.
            contar_notas_1(resto_5)
# Contar notas de 10 reais.
def contar_notas_10(valor10):
    # Limitar quantias a serem contadas como nota de 10, para ser somente valores abaixo de 50 reais.
    if valor10 >= 10 and valor10 < 50:
        #Criar Variavel e verificar quantidade de notas de 10 reais a serem sacadas.
        notas_10 = valor10 // 10
        # Mostrar quantidade de notas de 10 reais.
        print(f"{notas_10} de 10 reais")
        # Criar variável e calcular o resto que precisa ser calcula em notas de inferiores.
        resto_10 = valor10 % 10
        # Criar condições para as notas de valor inferior e chamar as fuções respectivas.
        if resto_10 >= 5 and resto_10 <= 9:
            contar_notas_5(resto_10)
        elif resto_10 < 5:
            contar_notas_1(resto_10)
# Contar notas de 50 reais.
def contar_notas_50(valor50):
    # Limitar quantias a serem contadas como nota de 50, para ser somente valores abaixo de 100 reais.
    if valor50 >= 50 and valor50 < 100:
        #Criar Variavel e verificar quantidade de notas de 50 reais a serem sacadas.
        notas_50 = valor50 // 50
        # Mostrar quantidade de notas de 50 reais.
        print(f"{notas_50} de 50 reais")
        # Criar variável e calcular o resto que precisa ser calcula em notas de inferiores.
        resto_50 = valor50 % 50
        # Criar condições para as notas de valor inferior e chamar as fuções respectivas.
        if resto_50 >= 10:
            contar_notas_10(resto_50)
        elif resto_50 >= 5:
            contar_notas_5(resto_50)
        elif resto_50 < 5:
            contar_notas_1(resto_50)
    # Criar condição para que valores menores de 50 reais passe para as funções das notas inferiores
    elif valor50 >= 0 and valor50 < 50:
        contar_notas_10(valor50)
# Contar notas de 100 reais.
def contar_notas_100(valor100):
    # Limitar quantias a serem contadas como nota de 100, para ser somente valores abaixo de 100 reais.
    if valor100 >= 100 and valor100 <= 600 :
        #Criar Variavel e verificar quantidade de notas de 100 reais a serem sacadas.
        notas_100 = valor100//100
        # Mostrar quantidade de notas de 100 reais.
        print(f"{notas_100} de 100 reais")
        # Criar variável e calcular o resto que precisa ser calcula em notas de inferiores.
        resto_100 = (valor100 % 100)
         # Criar condições para as notas de valor inferior e chamar as fuções respectivas.
        if resto_100 != 0:
            contar_notas_50(resto_100)
# Função para contagem das notas do valor total do saque.
def contar_notas_saque(saque):
    if saque >= 100 and saque <= 600:
        contar_notas_100(saque)
    elif saque >= 50 and saque < 100 :
        contar_notas_50(saque)
    elif saque >= 10 and saque < 50:
        contar_notas_10(saque)
# Entrar com o valor do saque
saque = int(input("Qual o valor do Saque desejado? "))    
# Condição para limitar o saque e chamar a função de contar as notas.
if saque >=10 and saque <= 600:
    # Primeiro enunciado da contagem das notas.
    print("O saque pode ser realizado com a seguinte quentidade de notas:")
    # Chamar contagem de notas.
    contar_notas_saque(saque)
else:
    # Negar operação porque está fora do limite do saque.
    print(f"O valor R$ {saque} não pode ser sacado.")