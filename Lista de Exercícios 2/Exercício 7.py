# Crie um algoritmo que calcule e mostre o novo valor de um salário a partir das seguintes regras: 
# salários de até R$ 1.000,00 inclusive recebem 30% de aumento,
#  salários de até R$ 2.000,00 inclusive recebem 25%, 
# salários de até R$ 3.000,00 inclusive recebem 20%, 
# salários de até R$ 4.000,00 inclusive recebem 15% e 
# salários acima de R$ 4.000,00 recebem 10%.
# Definir função
def calcular_salario_novo(valor):
    # Função mostrar para valor.
    def imprimir_salario_novo(salario_novo):
        print(f"O novo salário é de R$ {salario_novo}.")
    # Verifica o salário atual e faz o calculo necessário.
    if valor <= 1000 :
       salario_novo = round((valor * 1.3),2)
       imprimir_salario_novo(salario_novo)
    elif valor <= 2000 :
        salario_novo = round((valor * 1.25), 2)
        imprimir_salario_novo(salario_novo)
    elif valor <= 3000 :
        salario_novo = round((valor * 1.2), 2)
        imprimir_salario_novo(salario_novo)
    elif valor <= 4000 :
        salario_novo = round((valor * 1.15), 2)
        imprimir_salario_novo(salario_novo)
    elif valor < 0 :
        print("Salário inválido.")
    else :
        salario_novo = round((valor * 1.1), 2)
        imprimir_salario_novo(salario_novo)
# Inserir salário.
salario_atual = float(input("Insira o salário atual: "))
# Chamar função e mostrar resultado.
calcular_salario_novo(salario_atual)