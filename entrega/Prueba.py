#para este ejercicio la idea era que uses bucles anidados aca va el ejemplo
#supongamos que queremos imprimir
#@@@
#@@@
#@@@
#podríamos unsar un primer para indicar la cantidad de filas a imprimir en este caso 3
#for i in range(3 ):
#y usar otro for dentro de este (anidado para imprimir el carácter que nos queremos en este caso un@)
#for i in range(3):
#print('@')
#conclusión nos queda
a= ("#")
for i in range(6):    
    for j in range(6):
        
        print(a, end=' ')# imprime en la misma línea
#        print()#dejamos un espacio en blanco para cuando hace la próxima vuelta del for