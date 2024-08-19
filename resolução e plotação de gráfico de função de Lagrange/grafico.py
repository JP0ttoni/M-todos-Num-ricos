import numpy as np
import matplotlib.pyplot as plt

# Dados da tabela
x = np.array([-8, -5.71428571, -3.42857143, -1.14285714, 1.14285714, 3.42857143, 5.71428571, 8])
y = np.array([1.06635918, 0.80014487, 0.64216079, 0.54170856, 0.44962931, 0.39317197, 0.33772819, 0.31377657])

# Funções de Lagrange
def l0(x, i, x_values):
    result = 1.0
    for j in range(len(x_values)):
        if j != i:
            result *= (x - x_values[j]) / (x_values[i] - x_values[j])
    return result

def lagrange_polynomial(x, x_values, y_values):
    result = 0.0
    for i in range(len(x_values)):
        result += y_values[i] * l0(x, i, x_values)
    return result

# Calculando P(x) para os pontos x da tabela
x_values = np.linspace(-8, 8, 1000)
y_values = lagrange_polynomial(x_values, x, y)

# Plotando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'bo', label='Pontos dados')
plt.plot(x_values, y_values, 'r-', label='Polinômio interpolador de Lagrange')
plt.title('Interpolação de Lagrange')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('polinomio_interpolador_lagrange.png')
plt.show()
