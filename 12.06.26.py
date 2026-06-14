import random

# Ver el LATEX que prepare para entender el codigo y el nombre de algunas variables

exitos = 0
fracasos = 0

parametro_p = float(input("Ingrese el valor de P: "))

# Rangos [0.1,0.2,0.3 ... 1.0]
rangos = [0,0,0,0,0,0,0,0,0,0]


def contador_distribucion(aleatorio):
    if(aleatorio > 0 and aleatorio <= 0.1):
        rangos[0] += 1
    elif(aleatorio > 0.1 and aleatorio <= 0.2):
        rangos[1] += 1
    elif(aleatorio > 0.2 and aleatorio <= 0.3):
        rangos[2] += 1
    elif(aleatorio > 0.3 and aleatorio <= 0.4):
        rangos[3] += 1
    elif(aleatorio > 0.4 and aleatorio <= 0.5):
        rangos[4] += 1
    elif(aleatorio > 0.5 and aleatorio <= 0.6):
        rangos[5] += 1
    elif(aleatorio > 0.6 and aleatorio <= 0.7):
        rangos[6] += 1
    elif(aleatorio > 0.7 and aleatorio <= 0.8):
        rangos[7] += 1
    elif(aleatorio > 0.8 and aleatorio <= 0.9):
        rangos[8] += 1
    elif(aleatorio > 0.9 and aleatorio <= 1.0):
        rangos[9] += 1

for iterador in range(100):
    aleatorio = random.random()
    if(aleatorio <= parametro_p):
        exitos += 1
    else:
        fracasos += 1
    contador_distribucion(aleatorio)

# Para ser expresado en porcenaje
parametro_p *= 100

print("Exitos: ", exitos)
print("Fracasos: ", fracasos)
