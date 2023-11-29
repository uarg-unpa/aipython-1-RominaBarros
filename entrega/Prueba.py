#para este ejercicio la idea era que uses bucles anidados aca va el ejemplo
#supongamos que queremos imprimir
#@@@
#@@@
#@@@
#podríamos unsar un primer para indicar la cantidad de filas a imprimir en este caso 3
#for i in range(3 ):
#y usar otro for dentro de este (anidado para imprimir el carácter que nos queremos en este caso un@)
#for i in range(3):
#print('@')
#conclusión nos queda
a= ("#")
for i in range(6):    
    for j in range(6):
        a=a+a
print(a)#, end=' ')# imprime en la misma línea
#        print()#dejamos un espacio en blanco para cuando hace la próxima vuelta del for


#tp 3 ejercicio 10
#    print(i,j)
#    while( j <6):
#        print(i,j)
  #      j=j+1
 #   i=i+1    
#    print(i,j)

#numero=(1,2,3,4,5,6)
#num=(1,2,3,4,5,6)
#for elem in numero:
#    for elem in num:
#        print(numero,num,)
#print()    
numeros=[1,2,3,4,5,6]
for i in range(6):#rango de la longuitud de la lista     //esta forma te da los numeros una abajo del otro
    for j in range(6):#
        print(numeros[i][j])

#11. Escribir un programa que pida al usuario un número entero y muestre por              tp3
#pantalla un triángulo rectángulo como el que se muestra
#Si se ingresa el número 9, el resultado será
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1

#i=0
#j=0
#while (i<6):
num=int(input("ingrese un número: "))
suma=(" ")
for i  in range(num,1,-2):
    suma=suma + {i}
  #for i  in range(num,1,-2):
    print(f"{i} " )

#print("")

n=0
num=int(input("ingrese un número natural: "))
for  n in range  (num):
  n=n+num
  print(f"{n} + {num}= {n+num}" )
print(n)  

#14.Escribir un programa que recibe como entrada desde el usuario dos números             tp3
#enteros e imprimir todos los números pares entre ellos.

par=("")
num1=int(input("ingrese un 1° número : "))
num2=int(input("ingrese un 2° número : "))
if num1<num2:
  n=num1
  while num1 <= num2:
    if num1%2==0:
      par=num1+par
      num1=num1+1
print("la suma de los numero pares entre los dos numeros ingresado es:",par)  