#include <stdio.h>

int main()
{
    int num1 = 10, num2 = 20, *ptr1, *ptr2;
    ptr1 = &num2;
    ptr2 = &num1;

    printf("valor de num1: %d\n", num1);
    printf("valor de num2: %d\n", num2);
    printf("valor de ptr1: %d\n", *ptr1);
    printf("valor de ptr2: %d\n", *ptr2);

    ptr1 = &num1;
    ptr2 = &num2;
    puts("");
    printf("valor de num1: %d\n", num1);
    printf("valor de num2: %d\n", num2);
    printf("valor de ptr1: %d\n", *ptr1);
    printf("valor de ptr2: %d\n", *ptr2);
    return 0;
}
