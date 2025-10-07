#include <stdio.h>

int produto(int x, int y)
{
    if (x == 1)
    {
        return y;
    }
    if (x == 0)
    {
        return 0;
    }
    return y + produto(x - 1, y);
}

int main()
{
    int a1 = 5, b1 = 3;  // Resultado esperado: 15
    int a2 = 0, b2 = 10; // Resultado esperado: 0
    int a3 = 7, b3 = 1;  // Resultado esperado: 7
    int a4 = 4, b4 = 6;  // Resultado esperado: 24

    printf("--- Testando a função produto() ---\n");

    printf("Produto de %d x %d: %d (Esperado: 15)\n", a1, b1, produto(a1, b1));
    printf("Produto de %d x %d: %d (Esperado: 0)\n", a2, b2, produto(a2, b2));
    printf("Produto de %d x %d: %d (Esperado: 7)\n", a3, b3, produto(a3, b3));
    printf("Produto de %d x %d: %d (Esperado: 24)\n", a4, b4, produto(a4, b4));

    return 0;
}