#4. Obtenga dos números del usuario mediante input. Si a es mayor que b, devuelve a es mayor que b, si a es 
#   menor que b, devuelve a es menor que b de lo contrario, a es igual a b.

a=int(input("ingrese el número a: "))
b=int(input("ingrese el número b: "))
if a==b: 
    print("los números ingresados son iguales")
else:
    if a>b:
        print("el número a es mayor al numero b ")
    else:
        print("el número b es mayor al número a")    
