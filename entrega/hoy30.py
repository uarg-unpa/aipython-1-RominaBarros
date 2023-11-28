str1=" bienvenidos a AIPython "
print(f"cadena original{str1}")
str1=str1.upper()
print(f"cadena despues de usar la funcion upper {str1}")
str1=str1.lower()
print(f"cadena despues de usar la cadena lower {str1}")
str1=str1.title()
print(f"cadena despues de usar la funcion Title {str1}")
print(f"usando * en cadena {str1*3}")
print(f"la suma de los numeros es {2+4}")## se suma 2+4 al estar entre corchete y da el resultado
#REBANADAS
















#hoy 03/11/23
nota1=7
nota2=8
nota3=10
promedio=(nota1+nota2+nota3)/3
print(f"el promedio de {nota1},{nota2},{nota3}es{promedio} ")
#otra forma con while
cont=0
suma=0
while(cont<3):
    nota=int(input("ingrese nota: "))
    suma=suma+nota
    cont=cont+1
print(f"el promedio de {nota1},{nota2},{nota3}es{promedio} ")

for num in range(3):
    nota=int(input("ingrese....."))
    suma=suma+num

range(3) # [0,1,2]
range(-3,2)# [-3,-2,-1,0,1,]
range(1,7,2)  # [1,3,5]     1°num da el primer n°, el 2° num da hasta donde llega, y el 3° num da de cuanto en cuanto salta

for num in range(3):
    print(num)

for _ in range(3):
    print("un mensaje que se repite tres veces")

cadena="python"
for letra in cadena:
    print(letra)