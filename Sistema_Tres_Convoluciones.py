import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# Paso 1: Definir las señales
t = np.linspace(-10, 10, 1000)
f1 = np.where((t >= 0) & (t <= 3), 1, 0)  # Pulso rectangular
f2 = np.where((t >= 0) & (t <= 5), t, 0)
f3 = np.exp(-t**2)  # Señal exponencial decaída

# Paso 2: Calcular las convoluciones en cascada
c12 = convolve(f1, f2, mode='same') / sum(f1)
c123 = convolve(c12, f3, mode='same') / sum(f2)

# Paso 3: Graficar los resultados
plt.figure(figsize=(14, 10))

plt.subplot(5, 1, 1)
plt.plot(t, f1, label='Pulso Rectangular (f1)')
plt.legend()

plt.subplot(5, 1, 2)
plt.plot(t, f2, label='Señal Sinusoidal (f2)')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(t, f3, label='Señal Exponencial (f3)')
plt.legend()
plt.subplot(5, 1, 4)
plt.plot(t, c12, label='Señal Exponencial (f3)')
plt.legend()

plt.subplot(5, 1, 5)
plt.plot(t, c123, label='Convolución en Cascada (f1 * f2 * f3)')
plt.legend()

plt.xlabel('Tiempo t')
plt.suptitle('Convoluciones en Cascada y sus Señales')
plt.grid(True)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()