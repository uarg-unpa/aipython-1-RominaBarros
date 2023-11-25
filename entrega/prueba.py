#7. Genere un programa que clasifique a los estudiantes según sus puntuaciones:
#● 80-100, A;● 70-89, B; ● 60-69, C; ● 50-59, D; ● 0-49, F

nota =int(input("ingrese la puntuacion del alumno: "))
while nota>0 and nota<101:
    if nota <50:
	    print("la puntuación obtenida es F ")
else:
    if nota <60:
        print("la puntuación obtenida es D ")
    else:
	    if nota<70:
	        print("la puntuación obtenida es C ")
        else:
            if nota <80:
               	print("la puntuación obtenida es B ")
           	else:
		        print("la puntuación obtenida es A ")
