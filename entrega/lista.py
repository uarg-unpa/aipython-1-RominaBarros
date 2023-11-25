#lista vacia
numero=[7,8,9]
print(numero)
print(type(numero))# para saber que tipo es, en este caso int
nombre=[10,23.-89,39]
print(numero)
#vamos acceder a los elementos
primer_elemento=numero[0]
print(f"primer elemento:{primer_elemento}")
print(len(numero))
#recorrer la lista
for elem in numero:
    print(elem , end=",")
print()
#agregar elementos al final de la lista
numero[len(numero)-1]=100
print(numero)
numero[-1]=110
print(numero)
#no estamos sobreescribiendo el ultimo que no existe
#numero[4]=120
#print(numero)]
numero.append(4)
print(numero)
lista_regalos=["medias","vino","perfume"]
print(lista_regalos)
lista_regalos.append(["remera","galleta","carbon"])
print(lista_regalos)
#insert
numero.insert(1,23)#para remplazan el la posicion 1 por otro numero en este caso el 23
print(numero)
#index
indice=numero.index(110)
print(f"indice {indice}")

