num1=int(input("ingrese un número entero"))
num2=int(input("ingrese un segundo número entero"))
num3=int(input("ingrese un tercer número entero"))
suma=num1+num2+num3
prod=num1*num2*num3
print("la suma de los numeros es:", suma, "y el producto es: ", prod)
print(f"la suma es{suma}y el producto es{prod}")

#repetir lo anterior pero esta vez , para los tres numeros utilizar solo variable num
num=int(input("ingrese un numero: "))
con=1
suma=0
prod=1
while con <=3:
    suma=suma+num
    prod=prod*num
    num=int(input("ingrese otro numero"))
    con=con+1
print(f"la suma es{suma}")
print(f"el producto es {prod}")

##otra forma de hacerlo 
suma=0
producto=1
for _ in range(3)
    num=int(input("ingrese un numero:"))
    suma=suma+num
    prod=prod*num
    print(f"la suma es: {suma} y el producto es: {prod}")

#realizar un bucle que lea 5 numeros y escribir el menor de todos
        
menor=int(input("ingrese un numero: "))
con=1
num=menor
while 
    num<=menor:
    menor=num
    num=int(input("ingrese otro numero"))
    con=con+1
print(f"la suma es{suma}")
print(f"el producto es {prod}")
#otra opcion
menor=int(input("ingrese un numero: "))
for _ in range(4):
    num=int(input("ingrese numero"))
    if num<menor:
        menor=num
print(f"el menor de 5 numeros es:{menos}")

con=0
while cont<5:
    print(cont)
    cont=con+1
    if con==3:
        break

con=0    
while cont<5:
     if con==3:
         cont=con+1
         continue           #es una palabra reservada que vuelve a evaluar lo que esta arriba
     print(cont)
     cont=con+1