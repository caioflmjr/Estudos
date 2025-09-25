import numpy as np
from scipy.optimize import bisect, newton

#Dados

R = 140
L = 260e-3
C = 25e-6
vm = 24
im = 0.15
t = 0.0001

def g(f):
    om = 2 * np.pi * f
    termo_p = (om*L-1 /(om*C))**2
    termo_c = (vm**2)/(im**2) - R**2
    return termo_p - termo_c

f_bissec = bisect(g, 40, 70, xtol=t)

f_sec = newton(g, x0=50 ,x1=80, tol=t)

print(f"resultado com bisecção: f = {f_bissec:.4f} Hz")

print(f"resultado com secante: f = {f_sec:.4f} Hz")