import numpy as np

estoque = np.array([
    [10, 20, 30],
    [5, 10, 15]
])

precos = np.array([
    [2],
    [3],
    [4]
])

resultado = np.dot(estoque, precos)

print("Totais por loja:")
print(resultado)

total_geral = np.sum(resultado)

print("\nTotal geral:", total_geral)