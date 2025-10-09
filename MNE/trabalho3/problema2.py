import numpy as np

# --- Problema 2: Análise da Treliça ---
# (Usando os mesmos dados de antes)
alpha = np.sin(np.deg2rad(45))
A_trelica = np.array([
    # ... (cole a matriz A_trelica 17x17 aqui, como na resposta anterior) ...
    [-alpha, 0, 0, 1, alpha, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],       # Eq 1
    [-alpha, 0, -1, 0, -alpha, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],      # Eq 2
    [0, -1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],               # Eq 3
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],               # Eq 4
    [0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],               # Eq 5
    [0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],               # Eq 6
    [0, 0, 0, 0, -alpha, -1, 0, 0, alpha, 1, 0, 0, 0, 0, 0, 0, 0],      # Eq 7
    [0, 0, 0, 0, alpha, 0, 1, 0, alpha, 0, 0, 0, 0, 0, 0, 0, 0],      # Eq 8
    [0, 0, 0, 0, 0, 0, 0, -1, -alpha, 0, 0, 1, alpha, 0, 0, 0, 0],     # Eq 9
    [0, 0, 0, 0, 0, 0, 0, 0, -alpha, 0, -1, 0, -alpha, 0, 0, 0, 0],     # Eq 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0],               # Eq 11
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0],               # Eq 12
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, alpha, 0],          # Eq 13
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -alpha, 0],         # Eq 14
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -alpha, -1, 0, 0, 1],         # Eq 15
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, alpha, 0, 1, 0, 0],          # Eq 16
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -alpha, -1]          # Eq 17
])
b_trelica = np.array([0, 0, 0, 100000, 0, 0, 0, 150000, 0, 0, 0, 0, 0, 0, 0, 100000, 0])


# --- Método 1: Implementação da Eliminação de Gauss com Pivoteamento Parcial ---

def eliminacao_gauss_pivoteamento(A_in, b_in):
    A = A_in.copy().astype(float)
    b = b_in.copy().astype(float)
    n = len(b)

    # Fase de Eliminação Progressiva
    for i in range(n):
        # Pivoteamento: encontrar o maior pivô na coluna i
        pivo_max = i
        for k in range(i + 1, n):
            if abs(A[k, i]) > abs(A[pivo_max, i]):
                pivo_max = k
        # Trocar a linha atual com a linha do maior pivô
        A[[i, pivo_max]] = A[[pivo_max, i]]
        b[[i, pivo_max]] = b[[pivo_max, i]]

        # Zerar os elementos abaixo do pivô
        for k in range(i + 1, n):
            fator = A[k, i] / A[i, i]
            A[k, i:] = A[k, i:] - fator * A[i, i:]
            b[k] = b[k] - fator * b[i]

    # Fase de Substituição Reversa
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        soma = np.dot(A[i, i + 1:], x[i + 1:])
        x[i] = (b[i] - soma) / A[i, i]
        
    return x

print("--- Resolvendo com a nossa implementação de Eliminação de Gauss ---")
forcas_gauss_manual = eliminacao_gauss_pivoteamento(A_trelica, b_trelica)
for i, f in enumerate(forcas_gauss_manual):
    print(f"Força f{i+1}: {f:,.2f} N")


# --- Método 2: Implementação da Decomposição LU ---

def decomposicao_lu(A_in):
    # Implementação de PLU (pivoteamento parcial) para evitar divisões por zero
    A = A_in.copy().astype(float)
    n = A.shape[0]
    P = np.eye(n)
    L = np.zeros((n, n))
    U = A.copy()

    for i in range(n):
        # Encontrar o pivô máximo na coluna i (linhas i..n-1)
        pivo_max = i + np.argmax(np.abs(U[i:, i]))
        if abs(U[pivo_max, i]) < 1e-15:
            raise np.linalg.LinAlgError(f"Matriz singular ou pivô muito pequeno na coluna {i}")

        # Trocar linhas em U e em P
        if pivo_max != i:
            U[[i, pivo_max]] = U[[pivo_max, i]]
            P[[i, pivo_max]] = P[[pivo_max, i]]
            # Também trocar as linhas já computadas de L (colunas 0..i-1)
            if i > 0:
                L[[i, pivo_max], :i] = L[[pivo_max, i], :i]

        # Preencher L e zerar abaixo do pivô em U
        L[i, i] = 1.0
        for k in range(i + 1, n):
            L[k, i] = U[k, i] / U[i, i]
            U[k, i:] = U[k, i:] - L[k, i] * U[i, i:]

    return P, L, U

def resolver_lu(P, L, U, b_in):
    # Aplica a permutação P em b: Pb = P @ b
    b = b_in.copy().astype(float)
    Pb = P.dot(b)
    n = len(b)

    # Substituição Direta (Ly = Pb)
    y = np.zeros(n)
    for i in range(n):
        soma = np.dot(L[i, :i], y[:i])
        y[i] = (Pb[i] - soma) / L[i, i]

    # Substituição Reversa (Ux = y)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        soma = np.dot(U[i, i + 1:], x[i + 1:])
        x[i] = (y[i] - soma) / U[i, i]

    return x

print("\n--- Resolvendo com a nossa implementação de Decomposição LU ---")
P, L, U = decomposicao_lu(A_trelica)
forcas_lu_manual = resolver_lu(P, L, U, b_trelica)
for i, f in enumerate(forcas_lu_manual):
    print(f"Força f{i+1}: {f:,.2f} N")

# Verificando se os resultados são os mesmos
print("\nOs resultados dos dois métodos manuais são iguais?", np.allclose(forcas_gauss_manual, forcas_lu_manual))