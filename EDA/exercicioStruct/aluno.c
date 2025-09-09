#include <stdio.h>
#include <string.h>

#define MAX_STRING 50

typedef struct
{

    char nome[MAX_STRING];
    int matricula;
    float nota;

} Aluno;

int main()
{
    Aluno al;
    strcpy(al.nome, "cleitin pinto");
    al.matricula = 2424;
    al.nota = 6.9;
    Aluno *ptr;
    ptr = &al;

    printf("Nome do aluno: %s\nMatricula: %d\nNota: %.2f\n", ptr->nome, ptr->matricula, ptr->nota);

    return 0;
}
