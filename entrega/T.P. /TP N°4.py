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

#c. Agregar un elemento al final de la lista.
lista_frutas.append("pelón")
print(lista_frutas)









#11. Crear una lista de números del 1 al 10.
numeros=[1,2,3,4,5,6,7,8,9,10]
print(numeros)

#a. Imprimir los tres primeros números utilizando rebanadas.


#12. Crear una lista de letras (‘a’ hasta ‘j’)
letras=["a","b","c","d","e","f","g","h","i","j"]
print(letras)




#15. Crear la siguiente lista =>flores= [rosas, orquídea,lirio,tulipan, margarita, dalia, hortensia]
flores= ["rosas","orquídea","lirio","tulipan", "margarita", "dalia", "hortensia"]
print(flores)