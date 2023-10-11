import math
import random
import matplotlib.pyplot as plt

# Función para calcular la distancia euclidiana entre dos ciudades
def distancia(ciudad1, ciudad2):
    x1, y1 = ciudad1
    x2, y2 = ciudad2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Función de costo (longitud total del recorrido)
def costo(solucion, ciudades):
    costo_total = 0
    for i in range(len(solucion) - 1):
        ciudad_actual = ciudades[solucion[i]]
        ciudad_siguiente = ciudades[solucion[i + 1]]
        costo_total += distancia(ciudad_actual, ciudad_siguiente)
    # Agregar la distancia de regreso a la ciudad inicial
    costo_total += distancia(ciudades[solucion[-1]], ciudades[solucion[0]])
    return costo_total

# Función para generar una solución vecina (intercambia dos ciudades)
def solucion_vecina(solucion):
    nueva_solucion = list(solucion)
    i, j = random.sample(range(len(solucion)), 2)
    nueva_solucion[i], nueva_solucion[j] = nueva_solucion[j], nueva_solucion[i]
    return nueva_solucion

# Función de probabilidad para aceptar soluciones peores
def probabilidad_aceptacion(costo_actual, costo_vecino, temperatura):
    if costo_vecino < costo_actual:
        return 1.0
    return math.exp((costo_actual - costo_vecino) / temperatura)

# Algoritmo de recocido simulado para el TSP
def recocido_simulado(solucion_inicial, ciudades, temperatura_inicial, factor_enfriamiento, num_iteraciones):
    solucion_actual = solucion_inicial
    costo_actual = costo(solucion_actual, ciudades)
    mejor_solucion = solucion_actual
    mejor_costo = costo_actual
    
    for i in range(num_iteraciones):
        temperatura = temperatura_inicial / (1 + i)  # Decrementa la temperatura con el tiempo
        
        solucion_vecina_actual = solucion_vecina(solucion_actual)
        costo_vecina_actual = costo(solucion_vecina_actual, ciudades)
        
        if costo_vecina_actual < costo_actual or random.random() < probabilidad_aceptacion(costo_actual, costo_vecina_actual, temperatura):
            solucion_actual = solucion_vecina_actual
            costo_actual = costo_vecina_actual
        
        if costo_actual < mejor_costo:
            mejor_solucion = solucion_actual
            mejor_costo = costo_actual
    
    return mejor_solucion, mejor_costo

# Ejemplo de uso
if __name__ == "__main__":
    # Generar un conjunto de ciudades aleatorias
    num_ciudades = 10
    ciudades = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_ciudades)]
    
    # Generar una solución inicial aleatoria
    solucion_inicial = list(range(num_ciudades))
    random.shuffle(solucion_inicial)
    
    # Parámetros del recocido simulado
    temperatura_inicial = 1000.0
    factor_enfriamiento = 0.95
    num_iteraciones = 1000

    # Ejecutar el algoritmo de recocido simulado
    mejor_solucion, mejor_costo = recocido_simulado(solucion_inicial, ciudades, temperatura_inicial, factor_enfriamiento, num_iteraciones)

    # Imprimir la mejor ruta y su longitud
    print("Mejor ruta encontrada:", mejor_solucion)
    print("Longitud de la mejor ruta:", mejor_costo)

    # Crear una lista de coordenadas de las ciudades en el orden de la mejor ruta
    mejor_ruta_coordenadas = [ciudades[i] for i in mejor_solucion]
    mejor_ruta_coordenadas.append(mejor_ruta_coordenadas[0])  # Agregar la primera ciudad al final

    # Separar las coordenadas en listas de X e Y para el gráfico
    x, y = zip(*mejor_ruta_coordenadas)

    # Graficar las ciudades y la ruta
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, c='red', marker='o', label='Ciudades')
    plt.plot(x, y, linestyle='-', linewidth=2, c='blue', label='Mejor Ruta')
    plt.title('Mejor Ruta Encontrada para el TSP')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.legend()
    plt.grid(True)

    # Mostrar el gráfico
    plt.show()
