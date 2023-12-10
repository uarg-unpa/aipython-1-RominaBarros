
#TP N°5
#9. Escriba una función que multiplique los elementos de una lista de números.
def multi(lista):
    res=1
    for i in range(0, len(lista)):        
        res*=lista[i]
        print(res)
    return res    
lista=[2,3,4]
print(multi(lista)) 