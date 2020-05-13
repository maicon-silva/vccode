# Definir função para verificar se é ano bissexto.
def bissexto(ano):
    if ano % 400 == 0:
        return True
    elif ano % 4 == 0 and ano % 100 != 0:
        return True
    else:
        return False
# Definir função para verificar a quantidade de dias no mês.
def verificar_dia(mes, ano):
    # Meses com 31 dias.
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    # Meses com 30 dias.
    elif mes in [4, 6, 9, 11]:
        return 30
    # Verificcar se fevereiro tem 28 ou 29 dias.
    elif mes == 2:
        if bissexto(ano):
            return 29
        else:
            return 28
    else:
        return -1
# Verificar se a data é válida.
def validar_data(dia, mes, ano):
    if verificar_dia(mes, ano) >= dia and dia > 0:
        return True
    else:
        return False
# Inserir parametros da data.
dia = int(input("Insira o dia: "))
mes = int(input("Insira o mês: "))
ano = int(input("Insira o ano: "))
# Verificar a data obtitida pelas entradas anteriores.
if validar_data(dia, mes, ano):
    print(f"A data {dia}/{mes}/{ano} é valida!")
else:
    print(f"A data {dia}/{mes}/{ano} não é valida!")
