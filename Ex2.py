"""
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
"""
def contar_letra_a(texto):
    texto = texto.lower() 
    return texto.count('a')  

entrada = input("Digite uma palavra ou texto: ")

quantidade = contar_letra_a(entrada)
print(f"A letra 'a' aparece {quantidade} vez(es) em >{entrada}<.")
