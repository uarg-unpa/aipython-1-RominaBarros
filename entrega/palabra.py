def mostrarCarac(palabra):##funcion
    for i in range(len(palabra)):## coleccion de caracteres(range es la longitud de la palabra)
        print(palabra(i))

def contarVocales(palabra):
    cant=0
    for i in range(len(palabra)):
        if palabra[i]=="a"or palabra[i]=="e" or palabra[i]=="i" or palabra[i]=="o" or palabra[i]=="u":
            cant=cant+1
    return cant

def cantCons(palabra):
        cant=0
        for letra in palabra:         
             if letra !="a" and letra !="e" and letra !="i" and letra !="o" and letra !="u":
                  cant+=1 #es lo mismo que decir cant=cant+1
        return cant

def buscarSimbolo(simbolo,palabra):
     cont=0
     for letra in palabra:
        if simbolo== letra:
            return True
     return False
# otra forma
def buscarSimbolo(simbolo,palabra):
     for letra in palabra:
          if letra==simbolo:
               return True
     return False               

def invertirPalabra(palabra):
    return palabra[::-1]##de esta forma queda de atraz para adelante 
     

def main():
    while true:#este menu se habre hasta que el usuario no lo quiera usar mas
        palabra=input("ingrese una palabra:")
        print("1:mostrar caracteres")    
        print("2:cantidad de vocales")
        print("3:cantidad de consonantes")
        print("4: buscar un simbolo")
        op=int(input("ingrese su opinion:"))
        if op ==1:
             mostrarCarac(palabra)    
        elif op ==2:
             print(f"la cantidad de vocales en {palabra}es {contarVocales(palabra)}")        
        elif op==3:
             print(f"la cantidad de consonantes en {palabra}es contarCons")
        elif op==4:
             simbolo=input("ingrese para buscar:")
             print(f"el{simbolo}se encuentra en {palabra}")

        elif op==5:
            invertida=invertirPalabra(palabra)
            print(invertida)
        else:
            print("parece no haber ingresado una opcion disponible")
                

 ##            
##
    cont=input("desea continuar? s/n ")
    if cont=="s" or cont =="S":
        continue
    else:
        break
print("finalizado")

main()
#se define con una palabra lo que se quiere hacer, como buscar ubna letra o un simbolo, esto nos da modulacion, divide el problemas para plantear una solución.
# esto es la base para la programacion orientada a objetos y asi realizar cietas acciones,                            

