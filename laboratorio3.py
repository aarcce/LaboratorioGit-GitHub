#!/usr/bin/python3
# Juan Diego Arce Navarro
# Laboratorio 3
# Remplazar la direccion del archivo de texto de las lineas 15 y 20

if __name__ == "__main__":

    lista = []
    lista2 = []
    lista_minusculas = []
    palindromos = []

    try:
        lectura_archivo = open(
            "/home/juandiegoarce/Documents/Python/laboratorio3/entrada.txt", "r")
        string_unico = lectura_archivo.read()
        print("\"", string_unico, "\"","tiene los siguientes palíndromos internos:")
        lista.append(string_unico)
        lectura_archivo_lista = open(
            "/home/juandiegoarce/Documents/Python/laboratorio3/entrada.txt", "r")
        archivo_lista1 = lectura_archivo_lista.readlines()

        for linea in archivo_lista1:
            lista2.extend(linea.split())
        # Anade todas las palabras del archivo a una lista

        for palabra in lista2:
            palabras_minusculas = palabra.lower()
            lista_minusculas.append(palabras_minusculas)
        tamano_lista = len(lista_minusculas)
        # Convierte todos los caracteres de las palabras en minusculas
        for palindromo in lista_minusculas:
            if palindromo == palindromo[::-1]:
                print(palindromo, ": indice")
                palindromos.append(palindromo)
        # Revisa si las palabras son palindromos

    except FileNotFoundError:
        print("No se encontro el archivo")

    except PermissionError:
        print("El archivo no tiene permisos de lectura")

    # Manejo de excepciones
