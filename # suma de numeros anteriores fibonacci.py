# suma de numeros anteriores "fibonacci"

def fibonacci_iter(n):
    a=1
    b=1
    if n==1:
        print('0')
    elif n==2:
        print('0','1')
    else:
        print('0')
        print(a)
        print(b)
        for i in range(n-3):
            total = a + b
            b=a
            a= total
            print(total)
opc=0



while(opc!=-1):
    print("Menú: \n")
    print("Ingrese opción: \n")
    print("1 - fibonacci \n")
    print("2 - Finalizar \n")


    opc = int(input('Ingresa la opción:'))

    if(opc==1):
         
         n = int(input('Ingrese el numero'))
         fibonacci_iter(n)

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