#2. Compare su edad y mi edad usando if..else. ¿Quién es mayor (vos o yo)?, para el ingreso de la edad use input
#   (“Ingrese su edad:”)Use un condición anidada para: Imprimir año si la diferencia es de 1, sino años para 
#   diferencias mayores.Cuando las edades son iguales imprimir un mensaje personalizado,ser creativo!!
cont=0
i=0
edad=int(input("Mi edad es 36,para comparar, ingrese su edad: "))
if edad>36:
    i=edad-36
    print("usted es mayor que yo")
 #   for i in  edad():
    #    cont=cont+1
    print("tenemos ",i, "años de diferencia")
else:
    i=36-edad
    print("soy mayor que vos")
if edad==36:
    print("tenemos la misma edad, que copado. conocimos la vida sin telefono celular. y fuimos felices jugando afuera con los amigos y vecinos")
    