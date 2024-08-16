import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Definir el tiempo extendido para la convolución
t = np.linspace(0, 20, 10000)

# Señales de entrada
x1 = np.sin(t)
x2 = np.cos(t)
x3 = np.exp(-t)

# Señales de sistema
h1 = np.cos(t)
h2 = np.cos(t)
h3 = signal.unit_impulse(10000, 'mid')

# Calcular las convoluciones
y1_h1 = signal.convolve(x1, h1, mode='full')
y1_h1 = y1_h1[:len(t)] / np.max(y1_h1)

y2_h2 = signal.convolve(x2, h2, mode='full')
y2_h2 = y2_h2[:len(t)] / np.max(y2_h2)
y3_h3 = signal.convolve(x3, h3, mode='same') / sum(h3)

# Graficar
plt.figure(figsize=(12, 8))

# Señales de entrada y sistemas
plt.subplot(3, 1, 1)
plt.plot(t, x1, label='x1(t) = sin(t)')
plt.plot(t, x2, label='x2(t) = cos(t)')
plt.plot(t, x3, label='x3(t) = exp(-t)')
plt.title('Señales de entrada y sistemas')
plt.xlabel('Tiempo t')
plt.ylabel('Amplitud')

# Convoluciones
plt.subplot(3, 1, 2)
plt.plot(t, y1_h1, label='Convolución x1(t) * h1(t)')
plt.plot(t, y2_h2, label='Convolución x2(t) * h2(t)')
plt.plot(t, y3_h3, label='Convolución x3(t) * h3(t)')
plt.title('Convolución Convoluciones de las señales de entrada')
plt.xlabel('Tiempo t')
plt.ylabel('Amplitud')

plt.subplot(3, 1, 3)
plt.plot(t, y3_h3 + y2_h2 + y1_h1)
plt.title('Sistema de Tres Convoluciones')
plt.xlabel('Tiempo t')
plt.ylabel('Amplitud')

plt.tight_layout()
plt.show()