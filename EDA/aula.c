#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    FILE *fp;
    char ch;

    fp = fopen("aula.c", "r");
    if (fp == NULL)
    {
        printf("unable to open file\n");
        system("pause");
        exit(0);
    }
    while (1)
    {
        ch = fgetc(fp);
        if (ch == EOF)
            break;

        printf("%c", ch);
    }
    fclose(fp);
    return 0;
}
