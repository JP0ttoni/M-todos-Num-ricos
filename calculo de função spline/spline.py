import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Dados da Tabela 3
x_data = np.array([1.0, 1.25, 1.50, 1.75, 2.0])
y_data = np.array([5.1, 5.79, 6.53, 7.45, 8.46])

# Calculando a derivada da função g(x) para o primeiro e último ponto
g_prime = np.array([1.512, 2.215, 2.983, 3.852, 5.0])

# Criando a curva spline cúbica
spline = CubicSpline(x_data, y_data, bc_type=((1, g_prime[0]), (1, g_prime[-1])))

# Criando pontos para o gráfico
x = np.linspace(1.0, 2.0, 100)
y = spline(x)

# Plotando os resultados
plt.figure(figsize=(8, 6))
plt.plot(x_data, y_data, 'o', label='Pontos dados')
plt.plot(x, y, label='Curva Spline Cúbica')
plt.title('Interpolação com Curva Spline Cúbica')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('spline_cubica.png')
plt.show()
