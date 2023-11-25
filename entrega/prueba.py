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
