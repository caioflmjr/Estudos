import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

pasta_atual = Path('.') 

print("--- Conteúdo Completo (Usando Path) ---")
filenames = []
# 2. Lista todos os itens no diretório (iterdir)
for item in pasta_atual.iterdir():
    print(item.name) # .name retorna apenas o nome do arquivo/pasta
    if item.is_file() and item.suffix == '.txt':
        filenames.append(item.name)



deformacao = np.array([])
tensao = np.array([])
       
for name in filenames:
    print(f"Carregando dados do arquivo {name}")
    valor1, valor2 = np.loadtxt(name, skiprows= 1, usecols=(0,1), unpack=True)
    deformacao = np.concatenate((deformacao, valor1))
    tensao = np.concatenate((tensao, valor2))

print(f"Dados carregados. Número de pontos: {len(deformacao)}")

# 2. Calcular os Coeficientes (m e b)
# O resultado 'coeficientes' é uma lista [m, b]
coeficientes = np.polyfit(deformacao, tensao, 1)

# Extrair os valores
m = coeficientes[0] # Coeficiente Angular (Inclinação)
b = coeficientes[1] # Coeficiente Linear (Intercepto)

print(f"\n--- Coeficientes da Regressão ---")
print(f"Coeficiente Angular (m): {m:.2f}")
print(f"Coeficiente Linear (b): {b:.2f}")
print(f"Equação da Linha de Melhor Ajuste: y = {m:.2f}x + {b:.2f}")

# 3. Criar a função de ajuste
funcao_ajuste = np.poly1d(coeficientes)

# 4. Gerar os pontos Y na linha de ajuste
# Aplica a função de ajuste a cada ponto X (deformacao) para obter a tensão ajustada
tensao_ajustada = funcao_ajuste(deformacao)

# 5. Plotar o Gráfico
plt.figure(figsize=(10, 6))

# Plotar os pontos originais
# 'o': Plota círculos (pontos)
plt.plot(deformacao, tensao, 'o', label='Dados Originais', markersize=4, alpha=0.6)

# Plotar a curva de melhor ajuste
# 'r-': Plota uma linha vermelha
plt.plot(deformacao, tensao_ajustada, 'r-', 
         label=f'Curva de Ajuste (Linear) \n($y = {m:.2f}x + {b:.2f}$)', 
         linewidth=2)

# Configurar o gráfico
plt.title('Regressão Linear: Curva de Melhor Ajuste (Tensão x Deformação)')
plt.xlabel('Deformação (Eixo X)')
plt.ylabel('Tensão (Eixo Y)')
plt.legend(loc='best')
plt.grid(True)

# Salvar o gráfico (será mostrado acima)
plt.savefig('curva_de_melhor_ajuste.png')
print("\nGráfico 'curva_de_melhor_ajuste.png' gerado com sucesso. Verifique o resultado acima.")