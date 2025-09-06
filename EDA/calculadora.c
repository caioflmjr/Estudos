#include <stdio.h>

int main()
{
    int x = 0, y = 0, z = 1;
    char o, v;
    while (z)
    {
        printf("digite o primeiro numero da operação:");
        scanf(" %d", &x);
        printf("digite o segundo numero da operação:");
        scanf(" %d", &y);
        printf("digite qual operação(+-*/):");
        scanf(" %c", &o);
        switch (o)
        {
        case '+':
            printf("resposta: %d\n", x + y);
            break;
        case '-':
            printf("resposta: %d\n", x - y);
            break;
        case '*':
            printf("resposta: %d\n", x * y);
            break;
        case '/':
            if (y != 0)
                printf("resposta: %d\n", x / y);
            else
                printf("erro: divisão por zero!\n");
            break;
        default:
            printf("resposta invalida\n");
            break;
        }
        printf("quer realizar outra operação?(Y/n):");
        scanf(" %c", &v);
        if (v == 'n')
            z = 0;
    }
}