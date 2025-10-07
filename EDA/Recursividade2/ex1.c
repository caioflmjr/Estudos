#include <stdlib.h>

int soma(int n)
{
    if (n < 0)
    {
        n = abs(n);
    }
    if (n == 0)
    {
        return 0;
    }
    return (n % 10) + soma(n / 10);
}