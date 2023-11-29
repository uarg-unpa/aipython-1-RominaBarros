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