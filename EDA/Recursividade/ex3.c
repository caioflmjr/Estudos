#include <stdio.h>

long long int f(int n)
{
    if (n == 0)
    {
        return 0;
    }
    if (n == 1)
    {
        return 1;
    }
    long long int a = 0, b = 1, r = 0;
    for (size_t i = 2; i <= n; i++)
    {
        r = a + b;
        a = b;
        b = r;
    }
    return r;
}

int main()
{
    printf("--- Testes da Função Fibonacci Recursiva ---\n\n");

    // Teste 1: Casos Base (N=0 e N=1)
    printf("Teste F(0): %lld (Esperado: 0)\n", f(0));
    printf("Teste F(1): %lld (Esperado: 1)\n", f(1));

    // Teste 2: Primeiros Termos
    printf("Teste F(2): %lld (Esperado: 1)\n", f(2));
    printf("Teste F(3): %lld (Esperado: 2)\n", f(3));
    printf("Teste F(4): %lld (Esperado: 3)\n", f(4));
    printf("Teste F(5): %lld (Esperado: 5)\n", f(5));
    printf("Teste F(6): %lld (Esperado: 8)\n", f(6));

    // Teste 3: Termo Clássico (N=10)
    printf("Teste F(10): %lld (Esperado: 55)\n", f(10));

    // Teste 4: Um Termo Maior
    // Este termo pode demorar alguns milissegundos, dependendo do seu sistema.
    printf("Teste F(20): %lld (Esperado: 6765)\n", f(20));

    // Teste 5: Cuidado com overflow e tempo de execução!
    // Se você estiver usando long long int, F(45) deve ser 1134903170
    printf("Teste F(45): %lld\n", f(50000000));

    printf("\n--- Testes Concluídos ---\n");

    return 0;
}