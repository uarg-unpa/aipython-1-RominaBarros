
while condicion:
    sentencia1

#condicion es verdadera-> infinitas veces
#condiciobn es falsa-> nunca

cont=6                                  #cont=0
while cont!=5:
    cont=cont+1                         #con=con-1
    cont=1
    while cont<5:
    cont =cont-1                         #cont=con+1


#cual es el problema


suma=0
while cont <=10:
    suma=suma+cont
    cont=cont+1
    num=int (input())
    suma=0
    while (num!=0):
        print(num)
        suma=suma+num
        num=int(input())
        #enunciado1
    while condicion1:
        enunciado2
    enunciado3
    enunciado4


num=int(input())
while (num<10):
    print(f"el numero es{num}")
    num=num+1
    ##num=1 #9
    ##num=10#


    cont 
    while(cont<5):
        num=int(input())
        print(f_"el numero ingresadoes {num}")
        cont=cont+1

        opcion=input("ingrese opcion")
        while(opcion!="A"):
            print(opcion)
            opcion=input

cont=0
sumatoria=0
while (cont<=10):
    num=int(input())
    sumatoria=sumatoria+num
    cont=cont+1

contpar=0
contimpar=0
for_in range (20):
    num=int    











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
for _ in range(3):
    num=int(input("ingrese un numero:"))
    suma=suma+num
    prod=prod*num
    print(f"la suma es: {suma} y el producto es: {prod}")

#realizar un bucle que lea 5 numeros y escribir el menor de todos
        
menor=int(input("ingrese un numero: "))
con=1
num=menor
while con<5:
    num<=menor
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