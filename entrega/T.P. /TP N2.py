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

#3. Solicite al usuario una contraseña, utilizando input(“Ingrese su contraseña”), almacene esta contraseña en
#   una variable. Luego informar si la contraseña introducida coincide con la guardada sin tener en cuenta 
#   mayúsculas y minúsculas .
cont="romina"
contraseña=(input("ingrese su contraseña "))
contraseña=contraseña.lower()
if contraseña==cont: 
    print("la contraseña ingresada coincide con la predeterminada")
else:
    print("la contraseña no coincide con la predeterminada ")

#4. Obtenga dos números del usuario mediante input. Si a es mayor que b, devuelve a es mayor que b, si a es 
#   menor que b, devuelve a es menor que b de lo contrario, a es igual a b.

a=int(input("ingrese el número a: "))
b=int(input("ingrese el número b: "))
if a==b: 
    print("los números ingresados son iguales")
else:
    if a>b:
        print("el número a es mayor al numero b ")
    else:
        print("el número b es mayor al número a") 
        
#5. Escriba un programa que pida al usuario un número entero e indique si es par o impar. 

num=int(input("ingrese un número entero: "))
if num%2==0: 
    print("el número ingresado es par")
else:
    print("el número ingresado es impar ")    

#6. Escriba un programa que pida al usuario un número entero del 1 al 7 y muestre por pantalla a qué día de la
#  semana corresponde. Controlar que el número se encuentre dentro del rango [1-7], sino es así, mostrar un 
#mensaje. Por ejemplo, si se ingresa el número 2 la salida debe ser martes.
    
dia=int(input("ingrese un numero referido al dia de la semana: "))
if dia>0 and dia<8:
    if dia==1:
        print("el día ingresado es lunes")
    if dia==2:
        print("el día ingresado es martes")
    if dia==3:
        print("el día ingresado es miercoles")
    if dia==4:
        print("el día ingresado es jueves") 
    if dia==5:
        print("el día ingresado es viernes")
    if dia==6:
        print("el día ingresado es sabado")  
    if dia==7:
        print("el día ingresado es domingo")
else:
    print("el numero ingresado no corresponde a un día de la semana")  

#7. Genere un programa que clasifique a los estudiantes según sus puntuaciones:
#● 90-100, A;● 70-89, B; ● 60-69, C; ● 50-59, D; ● 0-49, F

nota =int(input("ingrese la puntuacion del alumno: "))
if nota>0 and nota<101:
    if nota>89:
        print("la puntuación obtenida es:'A' ")
    else:
        if nota>69:
            print("la puntuación obtenida es:'B' ")
        else:
            if nota >59:
                print("la puntuación obtenida es:'C' ")
            else:
                if nota>49:
                    print("la puntuación obtenida es:'D' ")
                else:
                    print("la puntuación obtenida es:'F' ")    

