#include <stdio.h>

int potencia(int x, int n)
{
    if (x == 1 || n == 0)
    {
        return 1;
    }

    return x * potencia(x, n - 1);
}

int main()
{
    int x1 = 2, n1 = 3;  // Esperado: 2^3 = 8
    int x2 = 5, n2 = 2;  // Esperado: 5^2 = 25
    int x3 = 10, n3 = 1; // Esperado: 10^1 = 10
    int x4 = 7, n4 = 0;  // Esperado: 7^0 = 1 (Se sua função lida com n=0)

    printf("--- Testando a função potencia(x, n) ---\n");

    // Assumindo que sua função de potência se chama potencia
    printf("%d elevado a %d: %d (Esperado: 8)\n", x1, n1, potencia(x1, n1));
    printf("%d elevado a %d: %d (Esperado: 25)\n", x2, n2, potencia(x2, n2));
    printf("%d elevado a %d: %d (Esperado: 10)\n", x3, n3, potencia(x3, n3));
    printf("%d elevado a %d: %d (Esperado: 1)\n", x4, n4, potencia(x4, n4));
    // Nota: 7^0 = 1, se sua função trata o caso base n=0 corretamente.

    return 0;
}