#include <stdio.h>
#include <stdlib.h>

// Nombre: Juan Diego Arce
// Laboratorio 2

int calcularMCD(int a, int b)
{
    int n;

    // Se calcula el máximo común divisor
    while (b != 0)
    {
        n = b;
        b = a % b;
        a = n;
    }
    return a;
}
int main(int argc, char *argv[])
{

    // Verifica la cantidad correcta de argumentos
    if (argc != 3)
    {
        printf("Error: Debe proporcionar exactamente dos números enteros.\n");
        return 1;
    }
    // Se convierten los argumentos a enteros
    int num1 = atoi(argv[1]);
    int num2 = atoi(argv[2]);

    // Se verifica que los números no sean negativos
    if (num1 < 0 || num2 < 0)
    {
        printf("Error: Los números deben ser no negativos.\n");
        return 1;
    }
    // Se verifica que los numeros no sean igual a cero
    if (num1 == 0 && num2 == 0)
    {
        printf("Error: Ambos números no pueden ser cero.\n");
        return 1;
    }
    // Se llama a la función que calcula el Máximo común divisor
    int mcd = calcularMCD(num1, num2);
    printf("El máximo común divisor de %d y %d es: %d\n", num1, num2, mcd);
    return 0;
}
