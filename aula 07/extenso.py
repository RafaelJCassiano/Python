from num2words import num2words
from os import system, name #importa biblioteca do sistema operacional  e o nome do sistema operacional              
#if ternario (if escrito em uma linha so, nao pode ter elif)
system('cls') if (name == 'nt') else system('clear')
numero=int(input('informe um numero '))
print(num2words(numero,lang='pt_BR'))