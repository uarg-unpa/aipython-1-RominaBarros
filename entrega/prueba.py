#7. Genere un programa que clasifique a los estudiantes según sus puntuaciones:
#● 80-100, A;● 70-89, B; ● 60-69, C; ● 50-59, D; ● 0-49, F

nota =int(input("ingrese la puntuacion del alumno: "))
while nota>0 and nota<101:
    if nota<=49:
        print("F")    
    if nota:
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
         
