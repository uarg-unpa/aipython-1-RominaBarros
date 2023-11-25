#9. Para pagar un determinado impuesto se debe ser mayor de 18 años y tener ingresos
#iguales o superiores a $100000 mensuales. Escribir un programa que pregunte al
#usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene
#que pagar o no el impuesto.

edad=int(input("ingrese su edad: "))
ingreso=int(input("ingrese su sueldo: "))
if edad>18:
    if ingreso>=100000:
	    print(" debe pagar el impuesto ")
else:
      print(" no debe pagar el impuesto ")     