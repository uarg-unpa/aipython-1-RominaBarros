numeros=[(1,2,3,),(4,5,6),(7,8,9)]
for i in range(len(numeros)):#rango de la longuitud de la lista     //esta forma te da los numeros una abajo del otro
    for j in range(len(numeros)):#
        print(numeros[i][j])

for fila in numeros:##otra forma        //por cada elemento en la coleccion
    for elemento in fila:     #         /te muestra como cada lista
        print(elemento,end=",")
    print()       

#funciones     def para invocar
def saludo():
    print("funcion a aipython")
lista=[1,2,3]
print(lista)
lista.append(33)
saludo()
del(lista[0]) 
print(lista)       