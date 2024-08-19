import numpy as np
import matplotlib.pyplot as plt

# Definição da função
def f(x, y):
    return -y + x + 2

# Solução exata
def exact_solution(x):
    return np.exp(-x) + x + 1

# Método de Runge-Kutta de 2ª ordem
def rk2(f, x0, y0, h, n):
    x = np.linspace(x0, x0 + n*h, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h, y[i] + h * k1)
        y[i+1] = y[i] + h * (k1 + k2) / 2
    return x, y

# Método de Runge-Kutta de 3ª ordem
def rk3(f, x0, y0, h, n):
    x = np.linspace(x0, x0 + n*h, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h/2, y[i] + h * k1 / 2)
        k3 = f(x[i] + h, y[i] + h * k2)
        y[i+1] = y[i] + h * (k1 + 4 * k2 + k3) / 6
    return x, y

# Método de Runge-Kutta de 4ª ordem
def rk4(f, x0, y0, h, n):
    x = np.linspace(x0, x0 + n*h, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h/2, y[i] + h * k1 / 2)
        k3 = f(x[i] + h/2, y[i] + h * k2 / 2)
        k4 = f(x[i] + h, y[i] + h * k3)
        y[i+1] = y[i] + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x, y

# Parâmetros
x0, y0 = 0, 2
h = 0.1
n = int(1 / h)

# Calculando as soluções
x_rk2, y_rk2 = rk2(f, x0, y0, h, n)
x_rk3, y_rk3 = rk3(f, x0, y0, h, n)
x_rk4, y_rk4 = rk4(f, x0, y0, h, n)
x_exact = np.linspace(x0, 1, 100)
y_exact = exact_solution(x_exact)

# Plotando os resultados
plt.figure(figsize=(10, 6))
plt.plot(x_exact, y_exact, label='Solução Exata', color='black', linewidth=2)
plt.plot(x_rk2, y_rk2, 'o-', label='RK2', color='red')
plt.plot(x_rk3, y_rk3, 's-', label='RK3', color='green')
plt.plot(x_rk4, y_rk4, '^-', label='RK4', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparação dos Métodos de Runge-Kutta com a Solução Exata')
plt.legend()
plt.grid(True)
plt.show()
