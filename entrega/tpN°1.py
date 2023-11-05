peso=input("ingrese su peso en kilos:")
peso=float(peso)
altura=input("ingrese su altura en metros:")
altura=float(altura)
imc=peso/(altura**2)
print("Tu índice de masa corporal es:",imc)
if imc<18.5:
    print("su imc está por de bajo de lo normal")
else:
    if imc>24.9:            
        print("su imc está por encima de lo normal")
    else:
        print("su imc está normal, usted es una persona saludable")    