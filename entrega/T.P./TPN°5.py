#1. Escribir una función que tome dos números y retorne la multiplicación entre ellos.
def producto (num1,num2):
    return num1*num2
print(f"El producto es:",(producto(5,5)))

#2. Modificar el ejercicio uno, en caso de que la invocación sea sin argumentos retorna
#siempre el producto de 1*1.
def producto (num1=1,num2=1):
    return num1*num2
res=producto()    
print(res)
print(f"El producto es:",(producto(5,5)))

#3. Crear una función que tome un nombre como parámetro y retorna un mensaje
#creativo.
def func(nombre="Romina"):
    return f"{nombre}, tu futuro lo haces con tus acciones"
res=func()
print(res)    
print(func("Franco"))

#4. Escribir una función que tome un número como entrada e imprima la tabla de
#multiplicar del 1 al 10, con el siguiente formato.
#4 x 1 = 4
def tabla(num=int):
  for i in range(1,11):
    print(f"{num} x {i} = {i*num}")               

tabla (8)

#5. Implementar una función que determine si dado un número este es par o impar.
def par_impar(num):
  if num%2==0:
    return "es par"
  else:
    return "no es par"

print ("es par??:",par_impar(55))

#6. Crear una función que calcule el factorial de un número.
def factor(num= 2):
  fac=1
  for i in range (1,num):
    fac *= i
#    print({fac}) #mostraria el resultado en cada buble  
  return fac
print(factor(5))
print(factor(8)) 

#7. Escribir una función que tome tres números como entrada y retorna el máximo.
def mayor_de_tres(num1, num2, num3):
  mayor=num1
  if num2 > mayor:
    mayor=num2
  if num3 > mayor:
    mayor=num3
  return mayor
print("el mayor de los números ingresados es: ",mayor_de_tres(4,9,11))

#8. Implementar una función que invierta un string.
#hola
#aloh
def invertir(texto):
    invertido = ""
    for i in range(len(texto) - 1, -1, -1):
        invertido += texto[i]
    return invertido 
print (invertir(" °_° nohtyP ed osruc °+°"))       

#9. Escriba una función que multiplique los elementos de una lista de números.
def multi(lista):
    for i in lista:
        res=1
        res*=lista[i]
        print(res)
    return res    
lista=[2,3,4]
print(multi(lista)) 

#10. Crear una función que tome un string como parámetro y verifique si es un
#palíndromo. Ejemplo: Arenera, Narran. etc.
def palindromo(pal):
  tamaño=(len(pal))
  pal = pal.lower
  com=0
  fin= len(pal)
  for i in range(0,tamaño):
    if pal(com)==pal(fin):
      com+=1
      fin-=1
    else:
      return False
  return True    
pal=input("ingrese una palabra: ")
print(palindromo(pal)) 
#                                         revisar por que no me da

#11. Implementar una función que convierte temperaturas de fahrenheit a celsius. =>[°C]=([°F]-32)*5/9
def grados(fahr):
  cel=float
  cel=((fahr)-32)*(5/9)
  return cel

fahr = float(input("ingrese la temperaturas en fahrenheit para convertir en celsius: "))
print("la temperatura ingresada es: ",grados(fahr),"grados celsius")

#12. Escribir una función que dada una lista de caracteres cuente la cantidad de vocales
#y retorne esa información.
def vocales(palabra):
  palabra= palabra.lower
  vocal=0
#  largo = int (len(palabra))
#  print (largo)
  for i in range(0,len(palabra)):
    if palabra[i]=="a" or palabra[i]=="e" or palabra[i]=="i" or palabra[i]=="o" or palabra[i]=="u":
      vocal += vocal 
      return vocal

palabra = str(input("ingrese una lista de caracteres: ")  ) 
print("la cantidad de vocales en los caracteres ingresados fueron: ", vocales(palabra))

#13. Escribir una función que tome dos listas como parámetros y las intercale en una
#nueva, retornar la nueva lista resultante.

lista1=[1,3,5,7,9]
lista2=[2,4,6,8]
l1=len(lista1)
l2=len(lista2)
if (l1)==(l2):
  l=len(lista1)
if l1<l2:
  l=l1
else:
  l=l2  
def intercalar(lista1, lista2):
  lista3=[]
  a=0
  for i in range (0,l):
    lista3[a]=lista1[i]
    a+=1
    lista3[a]=lista2[i]
    a+=1
    return lista3
print (intercalar(lista1,lista2))  ##por que no me funciona??

#14. Implementar una función que tome una lista de números y retorna el promedio de
#sus elementos.

def promedio(num):
  suma=0
  for i in range(0, len(num)):
    suma+=num[i]
  promedio=suma/len(num)  
  return promedio
num=[2,3,4,5,6,7]   
print (promedio(num)) 