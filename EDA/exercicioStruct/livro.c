#include <stdio.h>
#include <string.h>

#define MAX_STRING 50

typedef struct
{

    char titulo[MAX_STRING];
    char autor[MAX_STRING];
    int ano
} Livro;

int main()
{
    Livro livro1;
    strcpy(livro1.titulo, "daytrade dicas");
    strcpy(livro1.autor, "cleitin");
    livro1.ano = 2025;

    Livro *ptr;
    ptr = &livro1;

    printf("nome do livro: %s\nnome do autor: %s\nano de lançamento: %d\n", ptr->titulo, ptr->autor, ptr->ano);
    return 0;
}
