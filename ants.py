import random
import math

# Datos del problema
num_ciudades = 5
ciudades = [(0, 0), (2, 5), (3,0), (6, 6), (1, 7)]

# Parámetros del algoritmo
num_hormigas = 10
num_iteraciones = 100
alpha = 1.0  # Ponderación de feromonas
beta = 2.0   # Ponderación de distancia
evaporacion = 0.5
q = 100  # Cantidad de feromonas depositadas

# Inicialización de feromonas en las aristas
feromonas = [[1.0] * num_ciudades for _ in range(num_ciudades)]

# Función para calcular la distancia euclidiana entre dos ciudades
def calcular_distancia(ciudad1, ciudad2):
    x1, y1 = ciudad1
    x2, y2 = ciudad2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Función para que una hormiga construya una solución
def construir_solucion():
    solucion = [0]  # Comenzamos en la ciudad 0
    ciudades_disponibles = set(range(1, num_ciudades))
    
    while ciudades_disponibles:
        ciudad_actual = solucion[-1]
        probabilidades = []
        
        for ciudad in ciudades_disponibles:
            probabilidad = (feromonas[ciudad_actual][ciudad] ** alpha) * \
                           (1.0 / calcular_distancia(ciudades[ciudad_actual], ciudades[ciudad]) ** beta)
            probabilidades.append((ciudad, probabilidad))
        
        total_probabilidad = sum(prob[1] for prob in probabilidades)
        probabilidades = [(ciudad, prob / total_probabilidad) for ciudad, prob in probabilidades]
        
        siguiente_ciudad = random.choices(probabilidades)[0][0]
        solucion.append(siguiente_ciudad)
        ciudades_disponibles.remove(siguiente_ciudad)
    
    return solucion

# Función para calcular la longitud de una solución
def calcular_longitud(solucion):
    longitud = 0
    for i in range(num_ciudades - 1):
        longitud += calcular_distancia(ciudades[solucion[i]], ciudades[solucion[i+1]])
    longitud += calcular_distancia(ciudades[solucion[-1]], ciudades[solucion[0]])  # Volver a la ciudad de inicio
    return longitud

# Función para actualizar las feromonas en las aristas
def actualizar_feromonas(soluciones):
    for i in range(num_ciudades):
        for j in range(num_ciudades):
            if i != j:
                feromonas[i][j] *= evaporacion
    
    for solucion in soluciones:
        longitud = calcular_longitud(solucion)
        for i in range(num_ciudades - 1):
            ciudad_actual = solucion[i]
            siguiente_ciudad = solucion[i + 1]
            feromonas[ciudad_actual][siguiente_ciudad] += q / longitud
            feromonas[siguiente_ciudad][ciudad_actual] += q / longitud  # La matriz es simétrica

# Algoritmo de colonia de hormigas
mejor_solucion_global = None
mejor_longitud_global = float('inf')

for _ in range(num_iteraciones):
    soluciones = [construir_solucion() for _ in range(num_hormigas)]
    
    for solucion in soluciones:
        longitud = calcular_longitud(solucion)
        if longitud < mejor_longitud_global:
            mejor_solucion_global = solucion
            mejor_longitud_global = longitud

    actualizar_feromonas(soluciones)

print("Mejor solución encontrada:", mejor_solucion_global)
print("Longitud de la mejor solución:", mejor_longitud_global)
