# Os endereços IP versão 4 são divididos em cinco classes: A, B, C, D e E. 
# Os endereços no intervalo de 0 a 127 são classe A, de 128 a 191 são classe B, 
# de 192 a 223 são classe C, de 224 a 239 são classe D e a partir de 240 são classe E. 
# Crie um algoritmo que leia o primeiro octeto, no formato decimal, de um endereço IP e informe a sua classe.

# 1. Ler um valor decimal que represente o prmeiro octeto de um endereço IP.
primeiro_octeto = int(input("Insira o primeiro octeto do IP em formato decimal: "))

# 2. Dar o diagnóstico de que classe pertence o IP em questão.
if primeiro_octeto > 0 and primeiro_octeto < 128 :
    print("O IP pertence à classe A.")
elif primeiro_octeto >= 128 and primeiro_octeto < 192 :
    print("O IP pertence à classe B.")
elif primeiro_octeto >= 192 and primeiro_octeto < 224 :
    print("O IP pertence à classe C.")
elif primeiro_octeto >= 224 and primeiro_octeto < 240 :
    print("O IP pertence à classe D.")
elif primeiro_octeto >= 240 and primeiro_octeto <= 255 :
    print("O IP pertence à classe E.")
else:
    print("O endereço IP não existe, tente novamente com valores entre 1 e 255!")