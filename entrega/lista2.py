#lista con range            //desde 0, hasta el numero anterior al indicado
lrange=list(range(7))
print(lrange)
#remove                     //remueve el numero que se indica entre parentesis
lrange.remove(3)
print(lrange)
#reverse                    //hace que valla de atraz para adelante
lrange.reverse()
print(lrange)
#count
lrange.append(2)# agregre el numero 2
print(lrange.count(2))#para saber cuantas veces aparece un elemento de la lista
#sum, min, max
print(sum(lrange))#funciones por que no son exclusivas de la lista   //suma todos los numeros que aparecen en la lista
#del
del(lrange[2])#nos elimina el 4 que esta en el indice 2
print(lrange)
del(lrange)#nos elimina la lista
print(lrange)