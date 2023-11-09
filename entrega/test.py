print ("LAS MAQUINAS ME SORPRENDEN CON MUCHA FRECUENCIA")
print ()
print("hoy es viernes :)")
print ("23", '"23"')
print ('una computadora puede ser llamada "inteligente" si logra engañar a una persona haciendole creer que es un humano.')#"E"
print ("ROMINA","BARROS", 36) #F- entre los argumentos se pone coma y da como resultado un espacio
print ("ROMINA","BARROS", 36,sep="_") #"G"
print ("gregores", 988, 9400,"\t")#H
print ("gregores", 988, 9400, end="\n")# i - hace para que sea en otra linea????
print ("Feliz", "Primavera", 2023, "\n")
print ("Feliz","\n","Primavera","\n",2023,"\n")# permite imprimir en forma de escalera Feliz Primavera 2023
print ("              'solo podemos ver poco del futuro'  ")#
print ("pero lo suficiente para darnos cuenta de que hay mucho que hacer")
print ("    *")
print ("   * *")
print ("  *   *")
print (" *     *")
print ("***   ***")
print ("  *   *")
print ("  *   *")
print ("  *****")
print (5+7) #suma
print (0-9) #resta
print (2+45)
print (3/2) #division 
print (6**2) #potencia
print (3//2) # division que solo muestra el número entero del resultado "//"
x=4
y= x**2 + 6 * x + 9
print (y)
x=6
y= x**2 + 6*x + 9
print (y)
x=3
y= x**2 + 6*x + 9
print (y)

# EJERCICIO 3
#NO VAN ESTAS VARIABLES- primer@nombre - primer-nombre - primer$nombre, los string van entre comillas simples , dobles o triples
nombre="Romina" 
print("tu nombre es:",nombre) # variable nombre         EJEMPLO
nom ="Romina"
name="Romina"
apellido="Barros"
print("tu apellido es:",apellido)
ape="Barros"
last_name="Barros"
edad=36
print("tu edad es:",edad)
age=36
altura=1.65
print("tu altura es:",altura)
alt=1.65
tuAltura=1.65
estatura=1.65
vuelo=1540
print("el numero de vuelo es:",vuelo)
Num_Vuelo=1540
NumVuelo=1540
temperatura=21
print("la temperatura es:",temperatura)
temp=21
temp_amb=21
salario=200
print("el salario es:",salario)
salarioMensual=200
salMen=200
salarioMen=200
finJuego="fin"
theEnd="fin"
numeroPar=22
numero_par=4
numPar=2

#EJERCICIO N°5 input
print("ingrese su APELLIDO")                   
ape=input() # para que el usuario ingrese los datos                     

print("ingrese su nombre")                            
nom=input() # para que el usuario ingrese los datos                            

print("ingrese su edad")                                                     
edad=input() # para que el usuario ingrese los datos                            
print ("todas las personas con apellido ",ape," tienen un futuro prospero, ni hablar si se llaman ",nom,"y con ",edad, "años de edad, TENDRAS EL DOBLE DE FORTUNA ")
#5 B PREGUNTAR
ape, nom, edad=input()

#6
num1=input("ingrese un número:")
num1=int (num1)                         #si no se hace esta linea, lo toma como dos string
num2=input("ingrese otro numero: ")
num2=int (num2)                          #si no se hace esta linea, lo toma como dos string
print("la suma es:",num1+num2)
print("la resta es",num1-num2)
print("la multiplicacion es:",num1*num2)
print("la potencia es:",num1**num2)
print("el resto es",num1%num2)

#7-
num1=input("ingrese un número entero:")
num1=int(num1)                         #si no se hace esta linea, lo toma como dos string
num2=input("ingrese un numero real:")
num2=float(num2)                          #(si no se hace esta linea, lo toma como dos string
print("la suma es:",num1+num2)
print("la resta es",num1-num2)
print("la multiplicacion es:",num1*num2)
print("la potencia es:",num1**num2)
print("el resto es",num1%num2)

#(8)
long=input("ingrese longitud del rectangulo:")
long=float(long)                         #si no se hace esta linea, lo toma como dos string
ancho=input("ingrese el ancho del rectangulo:")
ancho=float(ancho)   
print("el perimetro del rectangulo es:",2*long+2*ancho)

print("el area del rectangulo es:",long*ancho)

radio=input("ingrese el radio del circulo:")
radio=float(radio)   
print("el perimetro del circulo es:",2*3,1415*radio)
print("el área del circulo es:",3,1415*(radio)**2)

# N°9
peso=input("ingrese su peso en kilos:")
peso=float(peso)
altura=input("ingrese su altura en metros:")
altura=float(altura)
imc=peso/(altura**2)
print("Tu índice de masa corporal es:",imc)
if imc<18.5:
    print("su imc está por de bajo de lo normal")
else:
    if imc>24.9:            
        print("su imc está por encima de lo normal")
    else:
        print("su imc está normal, usted es una persona saludable")  
#10
cel=input("ingrese la temperatura en grados celcius:")
cel=float(cel)
far=(cel * 9/5)+32      #(0 °C × 9/5) + 32 = 32 °F
print("la temperarura ingresada ",cel," celcius son: ",far,"fahrenheit")   

#11
hs=input("ingrese la cantidad de horas trabajadas: ")
hs=int(hs)
costohs=input("ingrese el costo de la horas trabajadas:")
costohs=float(costohs)

pago=(hs * costohs)      
print("por ",hs,"horas trabajadas a $",costohs,"pesos la hora, recibira un pago de:$",pago,"pesos")     

#12
dinero=input("ingrese la cantidad de dinero que quiere invertir: $")
dinero=float(dinero)
interes=input("ingrese el interes anual:")
interes=int(interes)
años=input("ingrese la cantidad de años que desea invertir:")
años=int(años)

capital=(dinero/100)*(1+(interes)**años)      
print("el capital obtenido fue de $ ",capital,"pesos, de un monto invertido de ",dinero,"pesos, con una taza de interes de:",interes,"a ",años, "años")

#13
suma=0
con=1
while(con<=10):
    prod=input("ingrese el precio del producto:")
    prod=float(prod)
    suma=suma+prod
    con=con+1
prom=suma/10      
print("el promedio de los diez productos ingresados fue ",prom)