#1. Solicite información del usuario mediante el uso de input(“Ingrese su edad: ”). Si el usuario tiene 18 años
#   o más, informar: tiene edad suficiente para conducir. Si tiene menos de 18 años,informe la cantidad de años 
#   que faltan.
edad=int(input("Ingrese su edad: "))
if edad>18:
    print("tiene edad suficiente para conducir")
else:
    print("para conducir, le faltan",18-edad,"años")    

#2. Compare su edad y mi edad usando if..else. ¿Quién es mayor (vos o yo)?, para el ingreso de la edad use input
#   (“Ingrese su edad:”)Use un condición anidada para: Imprimir año si la diferencia es de 1, sino años para 
#   diferencias mayores.Cuando las edades son iguales imprimir un mensaje personalizado,ser creativo!!

edad=int(input("Mi edad es 36,para comparar, ingrese su edad: "))
if edad==36: 
    print("lo mas lindo, que conocimos la vida sin telefono celular. y fuimos felices jugando afuera con los amigos y vecinos")
else:
    if edad>36:
        print("usted es mayor que yo")
        i=edad-36
    else:
        i=36-edad
        print("soy mayor que vos")
if i ==1:
    print("tenemos ",i, "año de diferencia")
else:
    print("tenemos ",i, "años de diferencia")    
