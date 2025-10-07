#include <stdio.h>

long int somavet(int *n, int qtde)
{
    if (qtde <= 0)
    {
        return 0;
    }
    return n[qtde - 1] + somavet(n, qtde - 1);
}