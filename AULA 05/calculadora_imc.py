from os import system #importa biblioteca do sistema operacional                
system('cls')
print(" Calculadora de IMC ".center(50,"*"))
print("\n") 
print("Informe o pesso (em Kg) ")
peso = input ("-> ")
if(peso.isdecimal()):
    peso = float(peso)#float transforma em decimal
else:
    print("Digitar um numero. ")
print("Informe a Altura  (em centimetros) ")
altura = input ("-> ")
if(altura.isdecimal()):
    altura = float(altura)
else:
    print("Digitar um numero. ")
print(type(altura))
altura=altura/100
imc = round (peso/ (altura**2),2)
print("\n IMC", imc)
if ( imc< 18.5):
   classificacao =  "Abaixo do peso"
elif (imc < 25):
    classificacao =  "Peso ideal"
elif (imc <30):
    classificacao =  "Sobre peso"
else :
    classificacao =  "Obesidade"
print("\n",classificacao,"\n" )
