print(22+33)# suma                      unarios
print(22-33)# resta                     unarios
print(22**33)# potencia                 ()primero los parentesis, luego la potencia 
print(22*33)# multiplicacion
print(22/33)# division
print(22%33)# modulo
print(22//33)# division entera, solo se visualiza la parte entera del resultado
color="rojo"
print (color)
suma=3+5
print(suma)
suma="3+5" #al escribir la suma entre parentesis, se imprimira literal
print(suma)
suma=3+5
print("suma")
#print(edad), la variable no esta definida previamente, asi que dara error cuando no esta definida ni lleva comillas
nombre="Romina"
apellido="Barros"
edad=36
# ES IGUAL QUE DECIR
nombre, apellido, edad="Romina", "Barros", 36
#print (nombre, apellido, edad="Romina", "Barros", 36") escribir el print para que se imprima, si no, no dara respuesta
print(nombre, apellido, edad)
# variables inmutables (cajas diferentes)
edad=40
print(id(edad))
edad=edad + 1
print (id(edad))

print("ingrese su edad")                                         #              *1 linea
edad=input() # para que el usuario ingrese los datos                            *2 linea
print ("su edad es", edad)
#input("  ")    ingreso de datos al programa, puede ser un string...
edad=input("ingrese su edad:")# es para combinar las dos primeras lineas        *1+*2 linea
print (edad)
