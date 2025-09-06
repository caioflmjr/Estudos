#include <stdio.h>

int main(int argc, char const *argv[])
{
    int num = 10, *ptr;
    ptr = &num;
    printf("valor antes do incremento %d\n", *ptr);

    *ptr += 1;

    printf("valor depois do incremento %d\n", *ptr);

    return 0;
}
