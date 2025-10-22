#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct Linha
{
    int indice;
    int pop;
} Linha;

// Esta função define se o dado 'a' é maior ou menor que o dado 'b'
int compara(const void *a, const void *b)
{
    // 1. Converter os ponteiros genéricos para ponteiros da sua struct
    const struct Linha *dado_a = (const struct Linha *)a;
    const struct Linha *dado_b = (const struct Linha *)b;

    // 2. Lógica de comparação (Exemplo: para ordenar em ordem crescente de 'valor')
    if (dado_a->pop < dado_b->pop)
    {
        return -1;
    }
    else if (dado_a->pop > dado_b->pop)
    {
        return 1;
    }
    else
    {
        return 0; // Valores iguais
    }
}

int main()
{
    FILE *entrada, *saida;
    entrada = fopen("indice.csv", "r");
    saida = fopen("qs.csv", "w");
    char buffer[135];
    Linha *array = (Linha *)malloc(5600 * sizeof(Linha));
    int i = 0;
    while (fgets(buffer, 135, entrada) != NULL)
    {
        sscanf(buffer, "%d;%d", &array[i].indice, &array[i].pop);
        i++;
    }

    // Ordenar somente os 'i' elementos lidos, não toda a capacidade alocada
    qsort(array, i, sizeof(Linha), compara);

    for (int j = 0; j < i; j++)
    {
        fprintf(saida, "%d;%d\n", array[j].indice, array[j].pop);
    }
    free(array);
    fclose(entrada), fclose(saida);
}