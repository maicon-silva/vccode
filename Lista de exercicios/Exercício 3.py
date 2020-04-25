# Crie um algoritmo que recebe o valor da altura e do peso de uma pessoa e retorna seu IMC. 
# Mostra a pessoa o que ela precisa escrever e pedi o nome.
print("Seja bem-vindo ao calculo de IMC!")
peso = float(input("Insira aqui o peso: "))
altura = float(input("Insira aqui a altura (m):"))
# Calcula o IMC e mostra o resltado.
imc = round(((peso)/(altura**2)),3)
print(f"O IMC é: {imc}!")