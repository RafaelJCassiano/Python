'''
      programa para mostrar numeros inteiros em extenso
      somente numeros 1 a 100
'''

from os import system, name #importa biblioteca do sistema operacional  e o nome do sistema operacional              
#if ternario (if escrito em uma linha so, nao pode ter elif)
system('cls') if (name == 'nt') else system('clear')

dezenas=["","","vinte","trinta","quarenta","cinquenta","sesenta","setenta", "oitenta","noventa"]
numeros= ("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze",
"quatorze","quinze","desesis","dezessete","dezoito","dezenove")
valor=input("informe um numero 0 a 99  ")
numerico=int(valor)
extenso=''
if (numerico<20):
    extenso = numeros[numerico]
elif(numerico<100):
    extenso=dezenas[int(valor[0:1])]
    if (valor[1:2]!="0"):
        extenso=f"{extenso} e {numeros[int(valor[1:2])]}"
print(extenso)