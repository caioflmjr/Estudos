#include <stdio.h>
#include <stdlib.h>

int *CriaVetInt(int quantidade)
{
    int *vet;
    vet = (int *)malloc(quantidade * sizeof(int));
    if (vet == NULL)
    {
        printf("alocação de memória não foi sucedida\n");
        return NULL;
    }
    return vet;
}

int *CriaFloatInt(int quantidade)
{
    int *vet;
    vet = (int *)malloc(quantidade * sizeof(float));
    if (vet == NULL)
    {
        printf("alocação de memória não foi sucedida\n");
        return NULL;
    }
    return vet;
}

int main()
{
    int n = 4000000000;
    int *vet;
    vet = CriaFloatInt(n);
    if (vet != NULL)
    {
        free(vet);
    }
}