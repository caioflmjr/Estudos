import numpy as np

#Exercício 1

print("Exercício 1:\n")

a = 14.75
b = -5.92
c = 61.4
d = 0.6*(a*b-c)

a_asr = a + ((a * b) / c) * (((a + d)**2) / np.sqrt(np.abs(a * b)))

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
