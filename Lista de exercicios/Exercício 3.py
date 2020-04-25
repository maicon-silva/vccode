# Crie um algoritmo que recebe um valor de temperatura em Celsius e o converte para Fahrenheit.
# Mostra a pessoa o que ela precisa escrever e pedi o nome.
print("Seja bem-vindo ao calculo de IMC!")
peso = float(input("Insira aqui o peso: "))
altura = float(input("Insira aqui a altura (m):"))
# Calcula o IMC e mostra o resltado.
imc = round(((peso)/(altura**2)),3)
print(f"O IMC é: {imc}!")