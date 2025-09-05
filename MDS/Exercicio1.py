import numpy as np

a = 14.75
b = -5.92
c = 61.4
d = 0.6*(a*b-c)

a_asr = a + ((a * b) / c) * (((a + d)**2) / np.sqrt(np.abs(a * b)))

b_asr = (d * np.exp(d/2)) + ((a * d + c * d) / ((25 / a) + (35 / b))) / (a + b + c + d)
print(f"O valor de d é {d}\nO resultado do item (a) é {a_asr}\nO resultado do item (b) é {b_asr}")
