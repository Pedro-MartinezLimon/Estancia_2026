import random

# Variables globales

p_degradacion = 0
p_sintesis = 0
total_moleculas = 0

mol_nuevas = 0
mol_degrad = 0

parametro_phi = 0

momentos_cambio  = []
moleculas_cambio = []
#================ Funciones ===============
def Generar():
    if(random.random() <= float((p_sintesis/100) * (10 ** (parametro_phi)))):
        return True
    else:
        return False

def Degradar():
    if(random.random() <= float(p_degradacion/100) * (10 ** (parametro_phi))):
        return True
    else:
        return False

#==================== main ===============
if __name__ == '__main__':
    p_sintesis = float(input("P de sintesis (1-100%): "))
    p_degradacion = float(input("P de Degradacion (1-100%): "))
    
    mol_nuevas = float(input("Moleculas producidas: "))
    mol_degrad = float(input("Moleculas degradadas: "))
    
    parametro_phi = -1 * float(input("Parametro phi (1 - 10): "))

    for iterador in range(10 ** int(abs(parametro_phi))):
        if(Generar()):
            total_moleculas += mol_nuevas

            momentos_cambio.append(iterador)
            moleculas_cambio.append(total_moleculas)
        elif(total_moleculas > 0 and Degradar()):
            total_moleculas -= mol_degrad

            if(total_moleculas < 0):
                total_moleculas = 0
            
            momentos_cambio.append(iterador)
            moleculas_cambio.append(total_moleculas)
    print("========= Resultados (momento (dt)|moleculas totales)=============")
    print(momentos_cambio)
    print(moleculas_cambio)