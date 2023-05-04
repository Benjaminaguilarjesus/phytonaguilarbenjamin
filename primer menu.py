def sum():
    limite =int(input("ingresa la cantidad de numeros que quieres sumar: "))
    contador = 0
    for i in range (limite):
        valor = int(input("ingresa el valor"))
        contador = valor + contador 
    return (contador)

def resta():
    limite =int(input("ingresa la cantidad de numeros que quieres restar: "))
    contador = 0
    for i in range (limite):
        valor = int(input("ingresa el valor"))
        contador = valor - contador 
    return (contador)

def multi():
    limite =int(input("ingresa la cantidad de numeros que quieres multiplicar: "))
    contador = 0
    for i in range (limite):
        valor = int(input("ingresa el valor"))
        contador = valor * contador 
    return (contador)


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
        print("La respuesta es", sum())
    elif(opc==2):
        a = int(input('Ingrese el primer numero'))
        b = int(input('Ingrese el segundo numero'))
        print("La respuesta es", resta())
    elif(opc==3):
        a = int(input('Ingrese el primer numero'))
        b = int(input('Ingrese el segundo numero'))
        print("La respuesta es", multi())
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
        
