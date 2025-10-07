import numpy as np

A = np.array([
    [4, -1, -1, 0, 0, 0, 0, 0, 0, 0],
    [-1, 4, 0, -1, 0, 0, 0, 0, 0, 0],
    [-1, 0, 4, -1, -1, 0, 0, 0, 0, 0],
    [0, -1, -1, 4, 0, -1, 0, 0, 0, 0],
    [0, 0, -1, 0, 4, -1, -1, 0, 0, 0],
    [0, 0, 0, -1, -1, 4, 0, -1, 0, 0],
    [0, 0, 0, 0, -1, 0, 4, -1, 0, 0],
    [0, 0, 0, 0, 0, -1, -1, 4, -1, 0],
    [0, 0, 0, 0, 0, 0, 0, -1, 4, -1],
    [0, 0, 0, 0, 0, 0, 0, 0, -1, 4]
])

# Vetor b
b = np.array([-110, -30, -40, -110, 0, -15, -90, -25, -55, -65])

x0 = np.full(10, 20.0)
tolerancia = 0.000001
max_iteracoes = 1000

# --- Método de Jacobi ---
def jacobi(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0.copy()
    x_novo = np.zeros(n)
    
    for k in range(max_iter):
        for i in range(n):
            soma = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x_novo[i] = (b[i] - soma) / A[i][i]
        
        erro = np.linalg.norm(x_novo - x) / np.linalg.norm(x_novo)
        x = x_novo.copy()
        
        if erro < tol:
            print(f"Jacobi convergiu em {k+1} iterações.")
            return x
            
    print("Jacobi não convergiu.")
    return x

# --- Método de Gauss-Seidel ---
def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0.copy()
    
    for k in range(max_iter):
        x_antigo = x.copy()
        for i in range(n):
            soma = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x[i] = (b[i] - soma) / A[i][i]
            
        erro = np.linalg.norm(x - x_antigo) / np.linalg.norm(x)
        
        if erro < tol:
            print(f"Gauss-Seidel convergiu em {k+1} iterações.")
            return x

    print("Gauss-Seidel não convergiu.")
    return x


solucao_jacobi = jacobi(A, b, x0, tolerancia, max_iteracoes)
print("Solução por Jacobi:", np.round(solucao_jacobi, 4))

solucao_gs = gauss_seidel(A, b, x0, tolerancia, max_iteracoes)
print("Solução por Gauss-Seidel:", np.round(solucao_gs, 4))