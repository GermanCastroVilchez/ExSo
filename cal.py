import sys
print("===============CALCULADORA=============")

operacion = 0


def opciones():
    print("OPCIONES")
    print("1- SUMA")
    print("2- RESTA")
    print("3- MULTIPLICACION")
    print("4- DIVISION")
    print("5- SALIR")


def principal():
    opciones()
    acumulador = 0
    numero = 0
    cantiN = 0
    operacion = int(input())
    print("Cantidad de Numeros")
    cantiN = int(input())

    if operacion == 1:
        print("==SUMA==")
        for x in range(cantiN):
            print("Ingrese numero", x + 1)
            numero = int(input())
            acumulador = acumulador + numero
            print(">>>>>", acumulador)
        print("Total = ", acumulador)
    elif operacion == 2:
        print("==RESTA==")
        for x in range(cantiN):
            print("Ingrese numero", x + 1)
            numero = int(input())
            acumulador = -acumulador - numero
            print(">>>>>>", acumulador)
        print("Total = ", acumulador)
    elif operacion == 3:
        print("==MUlTIPLICACION==")
        acumulador = 1
        for x in range(cantiN):
            print("Ingrese numero", x + 1)
            numero = int(input())
            acumulador = acumulador * numero
            print(">>>>>>", acumulador)
        print("Total =", acumulador)
    elif operacion == 4:
        print("==DIVISION==")

        for x in range(cantiN):
            print("Ingrese numero", x + 1)
            numero = int(input())
            if x == 0:
                acumulador = numero
                print(">>>>>>>>>>>>>>", acumulador)
            elif x >= 1:
                acumulador = acumulador / numero
                print(">>>>>>>>>>>>>>", acumulador)
        print("Total =", acumulador)
    elif operacion == 5:
        sys.exit(0)
    else:
        principal()

principal()
