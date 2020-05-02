# Crie um algoritmo que recebe um valor de temperatura em Celsius e o converte para Fahrenheit. 
print("Seja bem-vindo!")
print("Converta uma temperaura em graus Celcius (ºC) em Fahrenheit (ºF).")
# Variavel do Celcis e calculo para Fahrenheit e em seguidamostra reultado.
celcius = float(input("Digite a temperatura para conversão (ºC): "))
fahrenheit = round(((celcius*(9/5)+32)),2)
print(f"A temperatura de {celcius}ºC em Fahrenheit é {fahrenheit}ºF!")