#include <stdio.h>
int *CriaVetInt(int quantidade)
{
    int *vet = nullptr;
    vet = new int[quantidade];
    if (vet == NULL)
    {
        printf("alocação de memória não foi sucedida\n");
        return NULL;
    }
    return vet;
}

float *CriaFloatInt(int quantidade)
{
    float *vet = nullptr;
    vet = new float[quantidade];
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
    float *vet;
    vet = CriaFloatInt(n);
    if (vet != NULL)
    {
        delete[] vet;
    }
}