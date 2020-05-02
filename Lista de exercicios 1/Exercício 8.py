# Crie um algoritmo que calcule o novo valor de um salário a partir de um valor percentual de reajuste. 
# O valor atual do salário e o valor percentual do reajuste devem ser informados pelo usuário como, por exemplo, 7,3%.
print("Para calcular o reajuste salarial voce vai precisar do valor do salário atual e da porcentagem de aumento.")
# Variaveis com salario atual (base), porcetagem de aumento, valor a ser aumentado (salario_aumento) 
# e o salário reajustado como (salário_novo).
salario_base = float(input("Insira o valor salário atual, em reais: "))
porcentagem = (float(input("Insira a porcentagem de aumento (%): "))) / 100
salario_aumento = round((salario_base * porcentagem),2)
salario_novo = round((salario_base + salario_aumento),2)
# Mostra o salário com reajuste.
print(f"O salário com o reajuste será de R$ {salario_novo}.")