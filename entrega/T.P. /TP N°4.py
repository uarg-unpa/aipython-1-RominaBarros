#1. Declarar una lista vacía.
num=[]
print(num)
print(type(num)) ##DECLARA QUE ES UNA LISTA

#2. Declarar una lista con más de 7 elementos.
CAP=[11,"VEINTIDOS",33,44,55,66,77,"OCHENTA Y OCHO",99]
print(CAP)
print(type(CAP))

#3. Mostrar la longitud de una lista creada.
numeros=[(12,23,34,),(45,56,67),(78,89,90)]
for i in range(len(numeros)):               #           //esta forma te da los numeros una abajo del otro
    for j in range(len(numeros)):
        print(numeros[i][j])

#4. Crear una lista de tus frutas favoritas
#a. Imprimir la longitud.

lista_frutas=["manzana","banana","frutilla","naranja","durazno"]
print(lista_frutas)                                               #muestra la lista una fruta abajo de la otra  
for i in range(len(lista_frutas)):#                    //mustra una letra abajo del otra, de todas las palabras
    for j in range(len(lista_frutas)):
        print(lista_frutas[i][j])

#b. Eliminar el primer elemento de la lista.

lista_frutas.remove("manzana")
print(lista_frutas)                