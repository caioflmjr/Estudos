#include <stdio.h>
#include <string.h>
int main()
{
    FILE *dados, *saida;
    dados = fopen("dados.csv", "r");
    saida = fopen("indice.csv", "w");

    if (dados == NULL || saida == NULL)
    {
        printf("Erro ao abrir os arquivos.\n");
        return 1;
    }

    char buffer[100];
    char *token;
    int n = 1;
    fgets(buffer, 100, dados);
    while (fgets(buffer, 100, dados) != NULL)
    {
        for (int i = 1; i <= 5; i++)
        {
            if (i == 1)
            {
                token = strtok(buffer, ";");
            }
            else
            {
                token = strtok(NULL, ";");
            }
            if (token == NULL)
            {
                break; // Sai do loop 'for' e ignora o processamento desta linha
            }
        }
        fprintf(saida, "%d;%s", n, token);
        n++;
    }
}
