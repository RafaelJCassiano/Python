from os import system
system ('cls')
numero = input ('informe um numero: ')    
if (numero.isnumeric()==True):
    print('isto e um numero')
    numero = int(numero)
    if ((numero%2)==1):
        print("Este numero e impar")
        print(numero% 2)
    else:
        print('Este numero e par ')
else:
        print("Isto nao e um numero")
print ("Final de codigo")