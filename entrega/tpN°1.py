dinero=input("ingrese la cantidad de dinero que quiere invertir: $")
dinero=float(dinero)
interes=input("ingrese el costo del interes anual:")
interes=float(interes)
años=input("ingrese la cantidad de años que desea invertir:")
años=int(años)

capital=dinero(1+interes*años)      
print("el capital obtenido fue de $ ",capital,"pesos, de un monto invertido de ",dinero,"pesos, con una taza de interes de:",interes,"a ",años, "años")
M = C*(1 + i*n), donde “C” es el capital inicial, “i” es la tasa de interés aplicable a cada período y “n” es el número de períodos en que se generarán los intereses.
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
y el número de años, y muestre por pantalla el capital obtenido en la inversión