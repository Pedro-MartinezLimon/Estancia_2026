import random

# p : [0.0, 0.55) and q : [0.55, 1.0)
# La lógica y explicación estarán en el reporte que adjunte

p = print(input("Ingrese el valor de P: "))

if(p < 0 or p > 1):
    print("Ingrese un valor tal que p : [0,1]")

exitos = 0
fracasos = 0

for iterador in range(100):
    if(round(random) < p):
        exitos += 1
    else:
        fracasos += 1

print("Los exitos fueron: ", exitos, "los fracasos: ", fracasos)