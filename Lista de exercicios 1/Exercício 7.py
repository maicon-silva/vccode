# Crie um algoritmo que calcule a gorjeta a ser paga de uma conta de restaurante. 
# A gorjeta é calculada como sendo 10% do valor da conta, que deve ser informado pelo usuário.
print("Calcule  a gorjeta a ser paga pela cliente.")
sub_total = float(input("Digite o valor total da conta do cliente: "))
gorjeta = round((sub_total * 0.10),2)
total_c_gorjeta = round((sub_total + gorjeta), 2)

print(f"O valor da gorjeta é R$ {gorjeta}.")
print(f"O valor total com a gorjeta é R$ {total_c_gorjeta}.")