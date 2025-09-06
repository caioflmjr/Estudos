#include <stdio.h>

void atrptr(int num, int **ptr)
{
    *ptr = &num;
    printf("%d\n", num);
    printf("%p\n", &num);
    printf("%p\n", *ptr);
    printf("%d\n", **ptr);
}

int main()
{
    int numero = 20;
    int *pointer;
    atrptr(numero, &pointer);
    return 0;
}