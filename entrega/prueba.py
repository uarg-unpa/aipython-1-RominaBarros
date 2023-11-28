#14.Escribir un programa que recibe como entrada desde el usuario dos números
#enteros e imprimir todos los números pares entre ellos.

par=0
num1=int(input("ingrese un número 1 natural: "))
num2=int(input("ingrese un número 2 natural: "))
if num1<num2:
  n=num1
  while num1 <= num2:
    if n%2==0:
      par=num1+par
      n=n+1
print("la suma de los numero pares entre los dos numeros ingresado es:",n)  