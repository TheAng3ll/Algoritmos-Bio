import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo (2D)
np.random.seed(0)
datos_normales = np.random.randn(100, 2)  # Datos normales
datos_anomalos = np.random.randn(10, 2) + np.array([3, 3])  # Datos anómalos

# Combinar datos normales y anómalos
datos = np.vstack([datos_normales, datos_anomalos])

# Visualizar los datos
plt.scatter(datos[:, 0], datos[:, 1], c='b', marker='o', label='Datos Normales')
plt.scatter(datos_anomalos[:, 0], datos_anomalos[:, 1], c='r', marker='x', label='Anomalías')
plt.title('Detección de Anomalías con AIS')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.legend()
plt.grid(True)
plt.show()

# Implementación simple de AIS para detección de anomalías
def detectar_anomalias(datos, umbral):
    anomalias = []
    for dato in datos:
        distancia = np.linalg.norm(dato)  # Utiliza la distancia Euclidiana como medida de similitud
        if distancia > umbral:
            anomalias.append(dato)
    return np.array(anomalias)

# Umbral de detección de anomalías (ajusta según sea necesario)
umbral = 2.0

# Detección de anomalías
anomalias_detectadas = detectar_anomalias(datos, umbral)

# Visualizar las anomalías detectadas
plt.scatter(datos[:, 0], datos[:, 1], c='b', marker='o', label='Datos Normales')
plt.scatter(anomalias_detectadas[:, 0], anomalias_detectadas[:, 1], c='r', marker='x', label='Anomalías Detectadas')
plt.title('Anomalías Detectadas')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.legend()
plt.grid(True)
plt.show()

# Imprimir las anomalías detectadas
print("Anomalías Detectadas:")
for anomalia in anomalias_detectadas:
    print(anomalia)
