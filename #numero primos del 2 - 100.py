#"numero primos" 

def numeros_primos(n):
    for i in range(2, n+1):
        primo = True
        for j in range(2, i):
            if i == j:
                break
            elif i % j == 0:
                primo = False
            else:
                continue
        if primo == True:
            print(' ', i, end='')

        
opc=0
while(opc!=-1):
    print("Menú: \n")
    print("Ingrese opción: \n")
    print("1 - primos \n")
    print("2 - Finalizar \n")


    opc = int(input('Ingresa la opción:'))

    if(opc==1):
         n = int(input('¿Hasta qué número quieres la lista?: '))
         numeros_primos(n)

    elif(opc==2):
        print("Desea realizar una nueva operación?")
        a = input('si o no: ')
        if(a=="si"):
            opc=0
        else:
            opc=-1
            print("Programa finalizado")

    else:
        print("Opcion invalida")