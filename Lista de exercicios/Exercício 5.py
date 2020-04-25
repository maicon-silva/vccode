# Um motorista deseja abastecer um valor X em reais, de combustível.
# Escreva um algoritmo para ler o preço do litro do combustível e o 
# valor que o motorista deseja abastecer. Em seguida, informe quantos 
# litros foram abastecidos.

# Variavel preço da gasolina, ficou fixo.
valor_gasolina = float(3.675)
# Mostra o preço do litro de gasolina inserido.
print("Seja bem-vindo!")
print(f"O preço do litro de gasolina está a R$ {valor_gasolina}.")
# Variaveis do valor abastecido e da quantidade de litros que deram.
valor_abastecido = float(input("Qual o valor, em reais, voce deseja abastecer? "))
litros_abastecidos = round((valor_abastecido/valor_gasolina),3)
# Mostra a quantidade de litros abastecidos.
print(f"Voce abasteceu {litros_abastecidos} L de gasolina.")