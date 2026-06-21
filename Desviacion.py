import random

# Variables globales
almacenador_distribucion = []
def inicializar_alm_dis():
    for iterador in range(10):
        almacenador_distribucion[iterador] = 0

# Promedios
almacenador_promedios = []
def calcular_promedio(phi):
    suma = 0

    for iterador in range(10):
        suma += abs(almacenador_distribucion[iterador] * (0.1 * (iterador + 1)))
    return float(suma/(10 ** (phi + 1)))

# Varianza
almacenador_varianza = []
def calcular_varianza(phi, promedio_base):
    suma = 0

    for iterador in range(10):
        suma += abs((almacenador_distribucion[iterador] * (0.1 * (iterador + 1))) - promedio_base)
    return float(suma/(10 ** (phi + 1)))

# Triage aleatorios
def triage_aleatorios(aleatorio):
    if(aleatorio > 0 and aleatorio <= 0.1):
        almacenador_distribucion[0] += 1
    elif(aleatorio > 0.1 and aleatorio <= 0.2):
        almacenador_distribucion[1] += 1
    elif(aleatorio > 0.2 and aleatorio <= 0.3):
        almacenador_distribucion[2] += 1
    elif(aleatorio > 0.3 and aleatorio <= 0.4):
        almacenador_distribucion[3] += 1
    elif(aleatorio > 0.4 and aleatorio <= 0.5):
        almacenador_distribucion[4] += 1
    elif(aleatorio > 0.5 and aleatorio <= 0.6):
        almacenador_distribucion[5] += 1
    elif(aleatorio > 0.6 and aleatorio <= 0.7):
        almacenador_distribucion[6] += 1
    elif(aleatorio > 0.7 and aleatorio <= 0.8):
        almacenador_distribucion[7] += 1
    elif(aleatorio > 0.8 and aleatorio <= 0.9):
        almacenador_distribucion[8] += 1
    elif(aleatorio > 0.9 and aleatorio <= 1.0):
        almacenador_distribucion[9] += 1


if __name__ == '__main__':
    for iterador in range(10):
        almacenador_distribucion.append(0)

    for iterador_i in range(5):
        for iterador_k in range(10 ** (iterador_i + 1)):
            aleatorio = random.random()
            triage_aleatorios(aleatorio)

        print("Distribucion con ", 10 ** (iterador_i + 1))
        print(almacenador_distribucion)
        
        almacenador_promedios.append(float(calcular_promedio(iterador_i)))
        almacenador_varianza.append(float(calcular_varianza(iterador_i, almacenador_promedios[iterador_i])))
    
    inicializar_alm_dis()
    
    print("\n==================================Resultados=============================\n")

    print(almacenador_promedios)
    print(almacenador_varianza)