import matplotlib.pyplot as plt
import numpy as np
from trabalho2 import g

fteste = np.linspace(20, 200, 400)
valorg = g(fteste)

plt.figure(figsize=(10, 6))
plt.plot(fteste, valorg, label='g(f)')
plt.axhline(0, color='red', linestyle='--', label='Eixo y=0 (nossa raiz!)') # Linha do zero
plt.title('Gráfico da Função g(f) para Encontrar a Raiz')
plt.xlabel('Frequência (f) [Hz]')
plt.ylabel('Valor de g(f)')
plt.grid(True)
plt.legend()
plt.savefig('MNE/trabalho2/image.png')
plt.show()