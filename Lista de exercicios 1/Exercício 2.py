# Calculo de média ponderada de aluns com 3 notas.
# Primeiro tem a entrada do nome do professor e do aluno, com as respectivas variaveis 'nomeprof' e 'nomeal'
nomeprof = input("Olá, professor, insira seu nome para continuar: ")
print(f"{nomeprof}, seja bem-vindo!")
nomeal = input("Para continuar insira o nome do aluno ao lado: ")
print(f"Agora você pode adicionar as notas para a média do aluno(a), {nomeal}!")
print("O peso para media ponderada foram definidos como 1, 2 e 3, respectivaente para as notas 1, 2 e 3.")
# Aqui vão as variaveis para as notas e o peso das mesmas, sendo que 'n significa a nota e p significa peso' seguido pelo numero de ambos.
n1 = float(input("Insira a nota 1: "))
p1 = 1
n2 = float(input("Insira a nota 2: "))
p2 = 2
n3 = float(input("Insira o valor da nota 3: "))
p3 = 3
# Variável para o cálculo da média e em seguida a exibição do resultado.
mp = ((n1*p1)+(n2*p2)+(n3*p3))/(p1+p2+p3)
print(f"A média ponderada do aluno(a) {nomeal} é {mp}!")