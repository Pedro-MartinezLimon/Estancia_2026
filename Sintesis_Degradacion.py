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
    time_proteins = []
    # Store total proteins at one specific dt (i)
    total_proteins = 0

    birth_rate = int(input("Birth rate: "))
    death_rate = int(input("Death rate: "))

    # Exponent for delta t
    B_parameter = int(input("B (1-3): "))
    
    for i in range(10 ** (B_parameter)):
        if(Birth(birth_rate, B_parameter)):
            
            total_proteins += 1
        if(total_proteins > 0):
            death_count = 0

            for j in range(total_proteins):
                if(Death(death_rate, B_parameter)):
                    death_count += 1

            total_proteins -= death_count

        time_proteins.append(total_proteins)

    frecuencies_list = []

    for i in range(max(time_proteins) + 1):
        frecuencies_list.append(0)

    for k in range(len(time_proteins)):
        frecuencies_list[time_proteins[k]] += 1

    print(frecuencies_list)

#============= Proteins per delta time ===========

    plt.style.use('_mpl-gallery')

    fit, ax = plt.subplots()

    ax.stairs(time_proteins, linewidth=1.5)
    
    ax.set(xlim=(0, 10 ** (B_parameter)), xticks = np.arange(0, 10 ** (B_parameter)),
           ylim=(0, 30), yticks = np.arange(1, 30))
    
    plt.show()

#============= Frecuencies ===========

    x_axis = np.arange(len(frecuencies_list))

    # plot
    fig_1, ax_1 = plt.subplots()

    ax_1.bar(x_axis, frecuencies_list, width=1, edgecolor="white", linewidth=0.7)

    ax_1.set(xlim=(0, 20), xticks=np.arange(1, 20),
       ylim=(0, 100), yticks=np.arange(1, 100))

    plt.show()