import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do modelo
beta = 0.3
gamma = 0.1
rho = 0.1

# Condições iniciais
S0 = 0.93
I0 = 0.07
D0 = 0.0
R0 = 0.0
t0 = 0
tf = 150
h = 1  # passo de tempo

# Funções que representam as equações diferenciais
def dS_dt(S, I):
    return -beta * S * I

def dI_dt(S, I):
    return beta * S * I - (gamma / (1 - rho)) * I

def dD_dt(I):
    return (rho * gamma / (1 - rho)) * I

def dR_dt(I):
    return gamma * I

# Método de Euler
def euler_method(S0, I0, D0, R0, t0, tf, h):
    t_values = np.arange(t0, tf + h, h)
    S_values = np.zeros(len(t_values))
    I_values = np.zeros(len(t_values))
    D_values = np.zeros(len(t_values))
    R_values = np.zeros(len(t_values))
    
    S_values[0] = S0
    I_values[0] = I0
    D_values[0] = D0
    R_values[0] = R0

    for i in range(1, len(t_values)):
        S_values[i] = S_values[i-1] + h * dS_dt(S_values[i-1], I_values[i-1])
        I_values[i] = I_values[i-1] + h * dI_dt(S_values[i-1], I_values[i-1])
        D_values[i] = D_values[i-1] + h * dD_dt(I_values[i-1])
        R_values[i] = R_values[i-1] + h * dR_dt(I_values[i-1])
    
    return t_values, S_values, I_values, D_values, R_values

# Executar o Método de Euler
t, S, I, D, R = euler_method(S0, I0, D0, R0, t0, tf, h)

# Plotar os resultados
plt.figure(figsize=(12, 8))
plt.plot(t, S, label='Susceptíveis (S)')
plt.plot(t, I, label='Infectados (I)')
plt.plot(t, D, label='Óbitos (D)')
plt.plot(t, R, label='Recuperados (R)')
plt.xlabel('Tempo (dias)')
plt.ylabel('Proporção da População')
plt.legend()
plt.grid(True)
plt.title('Modelo SIDR da COVID-19 usando o Método de Euler')
plt.show()
