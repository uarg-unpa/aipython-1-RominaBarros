dinero=input("ingrese la cantidad de dinero que quiere invertir: $")
dinero=float(dinero)
interes=input("ingrese el interes anual:")
interes=int(interes)
años=input("ingrese la cantidad de años que desea invertir:")
años=int(años)

con=1
while(co):

capital=(dinero/100)*(1+(interes)**años)      
print("el capital obtenido fue de $ ",capital,"pesos, de un monto invertido de ",dinero,"pesos, con una taza de interes de:",interes,"a ",años, "años")
