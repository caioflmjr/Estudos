import numpy as np


def f(x):
    return x**3 - 9*x + 3


def cs(x):
    return "+" if x > 0 else "-"


def format_row(it, a, b, m, fa, fm, a_w=12, b_w=12, m_w=12):
    """Return a formatted table row string."""
    return f"{it:9d} | {a:{a_w}.6f} | {b:{b_w}.6f} | {m:{m_w}.6f} | {fa:2s} | {fm:2s}"


e = 10**-3
d = 1
a = 0
b = 1
k = 1

# print header
col_header = f"{'iter':>9s} | {'a':>12s} | {'b':>12s} | {'m':>12s} | {'fa':>2s} | {'fm':>2s}"
sep = "-" * len(col_header)
print(col_header)
print(sep)

while (d > e):
    m = (a + b) / 2
    d = np.abs(b - a)
    print(format_row(k, a, b, m, cs(f(a)), cs(f(m))))
    if f(a) * f(m) > 0:
        a = m
    else:
        b = m
    k += 1
