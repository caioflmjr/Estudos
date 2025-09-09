import numpy as np
import matplotlib.pyplot as plt

""" 

--- Identificação do grupo ---
Aluno 1: Caio Flávio de Lima Martins Júnior, Matrícula: 231011168
Aluno 2: Daniel da Silva Batista, Matrícula: 231011201
Aluno 3: Átila Sobral de Oliveira, Matrícula: 232014398
Aluno 4: Arthur Luiz Silva Guedes, Matriícula: 231028675
"""


#Exercício 1

print("Exercício 1:\n")

a = 14.75
b = -5.92
c = 61.4
d = 0.6*(a*b-c)

a_asr = a + ((a * b) / c) * ((a + d)**2 / np.sqrt(np.abs(a * b)))

b_asr = (d * np.exp(d/2)) + ((a * d + c * d) / ((25 / a) + (35 / b))) / (a + b + c + d)
print(f"O valor de d é {d}\nO resultado do item (a) é {a_asr}\nO resultado do item (b) é {b_asr}")

#Exercício 2 

print("\nExercício 2:\n")

vector = np.linspace(4, 61, 16)

print(f"{vector}") 

#Exercício 3

print("\nExercício 3:\n")

M = np.array([
    [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
    [3.0, 9.1667, 15.3333, 21.5, 27.6667, 33.8333, 40.0],
    [28.0, 27.75, 27.5, 27.25, 27.0, 26.75, 26.5],
    [6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0]
])

print(M)

#Exercício 4

print("\nExercício 4:\n")

a = 0.8

x = np.arange(-3, 3.1, 0.2)

y = (8 * a**2) / (x**2 + 4 * a**2)

plt.figure(figsize=(16,12))

plt.plot(x, y, marker='o', linestyle='-', color='b') 

plt.title('grafico de y versus x')
plt.xlabel('Vetor x')
plt.ylabel('Vetor y')
plt.grid(True)

plt.savefig('graficoexercicio4.png')

plt.show()

#Exercicio 5

def SItoING(cm, kg):

    pol = cm / 2.54
    lib = kg / 0.453592
    return round(pol, 2) , round(lib, 2)

altura = 183
massa = 92.3
ing = SItoING(altura, massa)

print(f"No padrão inglês você: \ntem {ing[0]} polegadas de altura \npesa {ing[1]} libras")
