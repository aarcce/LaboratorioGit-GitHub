#include <stdio.h>

// Nombre: Juan Diego Arce
// Laboratorio 1

void imprimirPiramide(int tamanoBase, int tipo, char caracter) {
    int i;
    int j;

    if (tipo == 1) {
        // Pirámide normal
        for (i = 1; i <= tamanoBase; i++) {
            // Espacios en blanco
            for (j = 1; j <= tamanoBase - i; j++) {
                printf(" ");
            }
            // Caracter de la pirámide
            for (j = 1; j <= 2 * i - 1; j++) {
                printf("%c", caracter);
            }
            printf("\n");
        }
    } else {
        // Pirámide invertida
        for (i = tamanoBase; i >= 1; i--) {
            // Espacios en blanco
            for (j = 1; j <= tamanoBase - i; j++) {
                printf(" ");
            }
            // Caracter de la pirámide
            for (j = 1; j <= 2 * i - 1; j++) {
                printf("%c", caracter);
            }
            printf("\n");
        }
    }
}

int main() {
    int tamanoBase, tipo;
    char caracter;
    char continuar;
    do {
        // Solicita al usuario el tamaño de la pirámide, el caracter a utilizar y el tipo de pirámide
        printf("\nIngrese el tamaño de la base de la pirámide: ");
        scanf("%d", &tamanoBase);

        printf("Ingrese el caracter que desea utilizar: ");
        scanf(" %c", &caracter);

        printf("\n1: Pirámide Normal \n2: Pirámide Invertida \n \nIngrese el tipo de pirámide que desea imprimir: ");
        scanf("%d", &tipo);

        // Imprime la pirámide
        imprimirPiramide(tamanoBase, tipo, caracter);

        // Pregunta si desea continuar
        printf("\nDesea continuar imprimiendo pirámides? \n\nNo: SALIR \nSi: Y\n\nDigite su respuesta: ");
        scanf(" %c", &continuar);

    } while (continuar == 'y' || continuar == 'Y');

    return 0;
}
