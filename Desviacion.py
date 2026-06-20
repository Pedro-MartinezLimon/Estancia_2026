import matplotlib.pyplot as ploter
import numpy
import random

# Contador de frecuencias
contador_frecuencias = list
def inicializar_frecuencias():
    for iterador_j in range(10):
        contador_frecuencias.append(iterador_j, 0)

# Variables globales
promedios = list
def calcular_promedio(num_aleatorios_generados):
    for iterador_i in range(10):
        suma += contador_frecuencias[iterador_i]
    return float(suma/num_aleatorios_generados)

variancias = list
def calcular_variancias(num_aleatorios_generado, promedio_a_comparar):
    for iterador_i in range(10):
        suma += (contador_frecuencias[iterador_i] - promedio_a_comparar)
    return float(suma/num_aleatorios_generado) 

# Clasifica las frecuencias
def triage_de_frec(aleatorio):
    for iterador_k in range(10):
        if(aleatorio > (0.1 * iterador_k) and aleatorio <= (0.1 (iterador_k + 1))):
            contador_frecuencias[iterador_k] += 1


if __name__ == '__main__':
    inicializar_frecuencias()

    for iterador_i in range(5):
        for iterador_k in range(10 * (iterador_i + 1)):
            triage_de_frec(random.random())

        promedios.append(iterador_i, calcular_promedio(10 * (iterador_i + 1))) 
        variancias.append(iterador_i, calcular_variancias(10 * (iterador_i + 1), promedios[iterador_i]))
        inicializar_frecuencias()
# ====================================== Generacion del plot ===================================================
    eje_x = 0.5 + numpy.arange(5)
    ploter.style.use('_mpl-gallery')

    fig, barra = ploter.subplots()

    barra.bar(eje_x, variancias, width = 1, edgecolor="white", linewidth=0.5)

    barra.set(xlim=(0, 5), xticks = numpy.arange(1, 10),
    ylim=(0, 5), yticks = numpy.arange(1, 5))


    ploter.show()