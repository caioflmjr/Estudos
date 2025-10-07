#include <stdio.h>
#include <string.h>

int verificaPalindromo(char *str, int c, int f)
{
    if (c >= f)
    {
        return 1;
    }
    if (str[c] != str[f])
    {
        return 0;
    }
    return verificaPalindromo(str, c + 1, f - 1);
}
int verificaPalindromoWrapper(char *str)
{
    int tamanho = strlen(str);
    if (tamanho == 0)
    {
        return 1; // Uma string vazia é um palíndromo
    }
    return verificaPalindromo(str, 0, tamanho - 1);
}

int main()
{
    char s1[] = "arara";                           // Palíndromo (1)
    char s2[] = "socorrammesubinoonibussemarocas"; // Palíndromo (1) - Clássico!
    char s3[] = "roma";                            // Nao Palíndromo (0)
    char s4[] = "ovo";                             // Palíndromo (1)
    char s5[] = "palindromo";                      // Nao Palíndromo (0)
    char s6[] = "";                                // Palíndromo (1) - String vazia

    printf("--- Testando a função verificaPalindromo() ---\n\n");

    printf("String: \"%s\" | Resultado: %d (Esperado: 1)\n", s1, verificaPalindromoWrapper(s1));
    printf("String: \"%s\" | Resultado: %d (Esperado: 1)\n", s2, verificaPalindromoWrapper(s2));
    printf("String: \"%s\" | Resultado: %d (Esperado: 0)\n", s3, verificaPalindromoWrapper(s3));
    printf("String: \"%s\" | Resultado: %d (Esperado: 1)\n", s4, verificaPalindromoWrapper(s4));
    printf("String: \"%s\" | Resultado: %d (Esperado: 0)\n", s5, verificaPalindromoWrapper(s5));
    printf("String: \"%s\" | Resultado: %d (Esperado: 1)\n", s6, verificaPalindromoWrapper(s6));

    return 0;
}
