#!/usr/bin/python3

#Nombre y carne
    #Juan Diego Arce 
    #C20655
#Descripcion
    #El programa solicita un caracter y el tamaño de la base superior para asi formar un triángulo. 

def programa():
    caracter = str(input("Digite el caracter por usar: "))                             #El programa inicia solicitanto un caracter y lo transforma en str (string)  .                    
    base = int(input("Digite el tamano de la base del triángulo superior: "))          #Luego solicita la base superior del triángulo y lo transforma a int (entero).
    for b in range(1, base+1):                                                         #Utiliza "b" para obtener una repetición hasta base+1 (1, 2, 3, 4, 5, base+1).
        for p in range(1, b+1):                                                        #Utiliza "p" para obtener la misma repetición pero esta vez hasta b+1.
            print(caracter, end="")                                                    #Imprime el caracter elegido por el usuario "p" veces.
        print(" ")
    for b in range(base-1, 0, -1):                                                     #Luego se repite el proceso pero esta vez de manera inversa para crear el triángulo infeior.
        for p in range (1,b+1):                                                        #Para que en el triángulo inferior no se repita la base se usa el range desde (base-1).
            print(caracter, end="")
        print(" ")
    opcion = input("Digite SALIR para salir, cualquier cosa para continuar: ")
    if opcion == "SALIR":                                                              #Se crea un pequeño menú para que el usuario decida si seguir creando triágulos o si desea salirse.
        print("Saliendo...")
        print("Saliste")      
    else:
        programa()

programa()
