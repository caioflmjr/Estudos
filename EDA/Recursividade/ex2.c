#include <stdio.h>

int strcomp(const char *a, const char *b)
{
    if (*a == '\0' && *b == '\0')
    {
        return 1;
    }
    if (*a != *b)
    {
        return 0;
    }

    return strcomp(a + 1, b + 1);
}

int main()
{
    const char *s1 = "teste";
    const char *s2 = "teste";
    const char *s3 = "testa";
    const char *s4 = "";
    const char *s5 = "";

    printf("'%s' e '%s': %d\n", s1, s2, strcomp(s1, s2)); // Saída: 1 (Iguais)
    printf("'%s' e '%s': %d\n", s1, s3, strcomp(s1, s3)); // Saída: 0 (Diferentes)
    printf("'%s' e '%s': %d\n", s4, s5, strcomp(s4, s5)); // Saída: 1 (Ambas vazias)
    printf("'%s' e '%s': %d\n", s1, s4, strcomp(s1, s4)); // Saída: 0 (Tamanhos diferentes)

    return 0;
}