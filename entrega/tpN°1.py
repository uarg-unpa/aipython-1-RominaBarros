#15
sociedad="aiPython P1"
mi_texto="aiPython P1"
toma=len(sociedad)
print(len (sociedad)) # asi se coloca la cantidad de string
#print("una ambiciosa"+"introduccion"+"a Python"+"parte uno" )
#toma=/en (sociedad)
sociedad=sociedad.upper()
print(sociedad )
sociedad=sociedad.lower()
print(sociedad )
sociedad=sociedad.title()
print(sociedad )

def tabla(num=7): 
    for i in range(1,11):   
        print(f"{i} x {num}={i*num}" )
print (tabla)        