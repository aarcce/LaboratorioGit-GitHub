#!/usr/bin/python3
# Nombre: Juan Diego Arce
# Laboratorio 2

def laboratorio2():

    lista = []  # Se crea una lista vacia.
    print(
        "Inserte la letra \"C\" cuando haya terminado "
        "de agregar los numeros a la lista")
    print(
        "Inserte los numeros que desea agregar a la lista uno por uno: ")

    continuar = True
    while continuar:  # Se utiliza while para ingresar varios numeros.
        numerosLista = input("")  # Se solicitan los numeros.
        if numerosLista != "C":  # Si inserta "C" el programa continua.
            numerosLista = int(numerosLista)  # Se convierte el input a entero.
            lista.append(numerosLista)  # Se añaden a la lista los números.
        else:
            continuar = False  # Se sale del while y continúa el programa.

    lista = sorted(lista)  # Se ordena la lista
    print("La lista ordenada es: {}".format(lista))  # Se imprime la lista.
    numeroM(lista)  # Se llama la siguiente funcion.


def numeroM(lista):

    T = 1  # Se define una variable para utilzar con el while.
    M = input("Inserte el numero \"M\": ")  # Se solicita el número M.
    M = int(M)  # Se convierte el número M a entero.
    while T == 1:  # Se utiliza el while para seguir solicitando el número M
        lista.append(M)  # Se agrega M a la lista
        lista = sorted(lista)  # Se ordena la lista
        indice = lista.index(M)  # Se busca el indice de M
        print("La lista ordenada es: {}".format(lista))  # Se imprime la lista
        print(
            "El indice de M es: {}".format(
                indice))  # Se imprime el indice de M
        T = T + 1  # Se modifica T para salir del while
        opcion = input(
            "Si no desea continuar digite \"SALIR\", "
            "si desea seguir ingresando numeros M "
            "digite cualquier caracter: ")
        if opcion != "SALIR":  # Si agrega un valor diferente a "SALIR"
            numeroM(lista)  # Se llama la funcion para comenzar
        else:
            print("Ha salido")  # Si el usuario ingresa "SALIR" termina


laboratorio2()
