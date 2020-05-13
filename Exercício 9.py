# Definir função para verificar o nome do mes com base no número e mostrar o resultado.
def nome_mes(mes):
    # Lista de meses.
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    # Verificar se o mês é válido e mostrar o nome corrspondente.
    if mes >= 1 and mes <= 12:
        print(f"O mês correspondente ao número {mes} é {meses[mes - 1]}.")
    else:
        print(f"O número {mes} não é válido como mês.")
# Entrada do número.
num_mes = int(input("Insira o número do mês que voce deseja procurar: "))
# Chamar a função.
nome_mes(num_mes)