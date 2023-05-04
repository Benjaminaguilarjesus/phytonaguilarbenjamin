def sum(a, b):
    c=a+b 
    return (c)

def resta(a,b):
    return (a-b)

def multi(a, b):
    return (a*b)


opc = 0 

while(opc!=-1):
    print("Menú: \n")
    print("Ingrese opción: \n")
    print("1 - Suma \n")
    print("2 - Resta \n")
    print("3 - Multi \n")
    print("4 - Finalizar \n")
    
    opc = int(input('Ingresa la opción:'))
    
    if(opc==1):
        a = int(input('Ingrese el primer numero'))
        b = int(input('Ingrese el segundo numero'))
        print("La respuesta es", sum(a,b))
    elif(opc==2):
        a = int(input('Ingrese el primer numero'))
        b = int(input('Ingrese el segundo numero'))
        print("La respuesta es", resta(a,b))
    elif(opc==3):
        a = int(input('Ingrese el primer numero'))
        b = int(input('Ingrese el segundo numero'))
        print("La respuesta es", multi(a,b))
    elif(opc==4):
        print("Desea realizar una nueva operación?")
        a = (input('Si o NO:'))
        if(a=="si"):
            opc=0
        else:
            opc=-1
            print(" programa Finalizado")
    else:
        print("opcion invalida")
        