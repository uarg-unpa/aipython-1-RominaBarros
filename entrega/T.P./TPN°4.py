#1. Declarar una lista vacía.
num=[]
print(num)
print(type(num)) ##DECLARA QUE ES UNA LISTA
print("")

#2. Declarar una lista con más de 7 elementos.
CAP=[11,"VEINTIDOS",33,44,55,66,77,"OCHENTA Y OCHO",99]
print(CAP)
print(type(CAP))
print("")

#3. Mostrar la longitud de una lista creada.
long=len (CAP)
print(long)
print("")

#4. Crear una lista de tus frutas favoritas
lista_frutas=["manzana","banana","frutilla","naranja","durazno"]
print(lista_frutas)                                               #muestra la lista una fruta abajo de la otra  
print("")

#a. Imprimir la longitud.
print("la longitud de la lista de frutas es:", len (lista_frutas))
print("")

#b. Eliminar el primer elemento de la lista.
del lista_frutas[0] #lista_frutas.remove("manzana") #otra forma de eliminar, pero con la palabra exacta
print(lista_frutas) 
print("")

#c. Agregar un elemento al final de la lista.
lista_frutas.append("pelón")
print(lista_frutas)
print("")

#d. Imprimir los resultados anteriores.
print(lista_frutas)
print("")

#5. Dada una lista mostrar el primer elemento, el del medio y el último.
print(lista_frutas)
print(lista_frutas[0])
medio=int(len (lista_frutas)/2)
print(lista_frutas[medio])
print(lista_frutas[len(lista_frutas)-1])
print("")

#6. Declarar una lista llamada datos_personales, insertar tu nombre, edad, altura,
#estado civil y dirección.
datos_personales=["ROMINA", 36, 1.56, "soltera","cepeda 7"]

#7. Almacenar los nombres de tus compañías favoritas en una lista dándole esos datos
#como inicial.
favorita=["fantoche","bon o bon","macucas","okebon","felford","block",]
print(favorita)
print("")

#8. Recorrer la lista del ejercicio 6 y mostrar los datos con print.
print(datos_personales)
print("")

#9. Recorrer la lista del ejercicio 6 y mostrar el índice más el nombre de la compañía.
for i in range (len(favorita)):
    print("indice: ", favorita.index(favorita[i]),"compañia:", favorita[i] )
print("")

#10. Modificar alguna/as de las compañía/s de la lista del ejercicio 6 y luego mostrar la
#lista. 
favorita[3]="terrabusi"
favorita.remove("macucas")
print(favorita)
print("")

#11. Crear una lista de números del 1 al 10.
numeros=[]
for i in range(1,11):
    numeros.append(i)
    #print(numeros)#muestra como van apareciendo los numeros mientras los agregan

#a. Imprimir los tres primeros números utilizando rebanadas.   
print(numeros[0:3])
print("")

#12. Crear una lista de letras (‘a’ hasta ‘j’)
letras=["a","b","c","d","e","f","g","h","i","j"]
print(letras)
print("")

#a. Imprima cada segundo elemento usando rebanadas.
for i in range(2, len(letras), 2):
    print(letras[: i], end=" ") 
print("")    

#13. Crear una lista a su criterio.
fam=["CRISTIAN","ROMINA","MARIANO","THIAGO"]

#a. Imprimir la lista en forma inversa usando rebanadas.
fam.reverse()
print(fam)
print("")

#14. Crear una lista de tus palabras favoritas
fav=["hamburguesas","milanesas","sopa","budin","helado"]
print(fav)
print("")

#a. Extraer una sub lista conteniendo desde la segunda hasta la cuarta palabra.
subfav=fav[1:4]
print(subfav)
print("")

#15. Crear la siguiente lista
#flores= [rosas, orquídea,lirio,tulipan, margarita, dalia, hortensia]
flores= ["rosas","orquídea","lirio","tulipan", "margarita","dalia", "hortensia"]

#a. Mostrar tres elementos desde el tercer elemento.
print(flores[2:5])
print("")  

#b. Mostrar los elementos en posiciones pares desde la segunda posición
for i in range(1,7,2):
    print(flores[i])
print("")    

#c. Mostrar todos los elementos desde la primera posición saltando de a tres elementos.
for i in range(0,7,3):
    print(flores[i])
print("")  