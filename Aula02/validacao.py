"""
Calcular a area de retangulo
"""
print("** Calcular area do retangulo **\n")

print("digite o Primeiro lado")
lado1 =  input()
print("Informe segundo lado")
lado2 = input()
#variavel.isnumeric = verifica se on valor pode ser numero inteiro
#variavel.isdecimal = verefica se o valor pode ser numero decimal
#print(type(lado1))
print("O primeiro valor e numero? ",lado1.isnumeric())
print("O segundo valor é numero inteiro? ", lado2.isnumeric())
#int = transforma o valor em um inteiro
#float transforma o valor da variavel em float (decimal)

print("Será que vai dar certo ou vai dar erro? ")
area=int(lado1)* int(lado2)
print("A area do retangulo é {} m² sendo os lados de {} X {}" .format(area,lado1,lado2))     


