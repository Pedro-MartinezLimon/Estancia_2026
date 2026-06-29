import matplotlib.pyplot as plt
import numpy as np
import random

# ================= Functions ===============
def Birth(birth_rate, B_parameter):
    if(random.random() <= float(birth_rate * (10 ** -B_parameter))):
        return True
    else:
        return False
def Death(death_rate, B_parameter):
    if(random.random() <= float(death_rate * (10 ** -B_parameter))):
        return True
    else:
        return False
# ================= Main ===============
if __name__ == '__main__':

    # Stores total of proteins every dt
    frecuencies = []
    for local_i in range(20):
        frecuencies.append(0)
    
    # Store total proteins at one specific dt (i)
    total_proteins = 0

    birth_rate = int(input("Birth rate: "))
    death_rate = int(input("Death rate: "))

    # Exponent of delta t
    B_parameter = int(input("B (1-3): "))

    for i in range(10 ** B_parameter):
        if(Birth(birth_rate, B_parameter)):
            total_proteins += 1

        if(total_proteins > 0):
            death_count = 0

            for j in range(total_proteins):
                if(Death(death_rate, B_parameter)):
                    death_count += 1
            total_proteins -= death_count
        
        frecuencies[total_proteins] += 1

    print(frecuencies)
    for i in range(len(frecuencies)):
        frecuencies[i] *= 10 ** -1
    print(frecuencies)


    plt.style.use('_mpl-gallery')

    # make data:
    x_axis = np.arange(len(frecuencies))

    # plot
    fig, ax = plt.subplots()

    ax.bar(x_axis, frecuencies, width=1, edgecolor="white", linewidth=0.7)

    ax.set(xlim=(0, 20), xticks=np.arange(1, 20),
       ylim=(0, 10), yticks=np.arange(1, 10))

    plt.show()