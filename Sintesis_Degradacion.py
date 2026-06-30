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
    Time = int(input("Time: "))
    B_parameter = int(input("B (1-3): "))
    
    for i in range(Time * 10 ** (B_parameter)):
        if(Birth(birth_rate, B_parameter)):
            total_proteins += 1

        if(total_proteins > 0):
            death_count = 0

            for j in range(total_proteins):
                if(Death(death_rate, B_parameter)):
                    death_count += 1

            total_proteins -= death_count

        time_proteins.append(total_proteins)

# Prepare a list to store the frecuencies of proteins 
    frecuencies_list = []

    for i in range(max(time_proteins) + 1):
        frecuencies_list.append(0)

    for k in range(len(time_proteins)):
        frecuencies_list[time_proteins[k]] += 1

    print("============= Frecuencies =====================")
    print(frecuencies_list)

#============= Proteins per delta time ===========

    plt.style.use('_mpl-gallery')

    fit, ax = plt.subplots()

    ax.stairs(time_proteins, linewidth=1.5, label="Proteins through the time")
    
    ax.set(xlim=(0, 10 ** (B_parameter)), xticks = np.arange(0, 10 ** (B_parameter)),
           ylim=(0, 10), yticks = np.arange(1, 10))
    
    plt.legend(loc="upper right")
    plt.title("Proteins distribution through time")

    plt.xlabel("delta t", fontsize=11)
    plt.ylabel("Proteins", fontsize=11)


    plt.tight_layout()
    plt.show()
    
    time_proteins.clear()
#============= Frecuencies ===========


    x_axis = np.arange(len(frecuencies_list))

    # plot
    fig_1, ax_1 = plt.subplots()

    ax_1.bar(x_axis, frecuencies_list, width=1, edgecolor="white", linewidth=0.7)

    ax_1.set(xlim=(0, 20), xticks=np.arange(1, 20),
       ylim=(0, Time * 100), yticks=np.arange(1, Time * 100))

    plt.title("Frecuencies")

    plt.xlabel("Number of proteins", fontsize=11)
    plt.ylabel("Frecuencie", fontsize=11)


    plt.tight_layout()
    plt.show()

#============== Normalization =============

summation_frecuencies = 0
summation_normalization = 0

for i in range(len(frecuencies_list)):
    summation_frecuencies += frecuencies_list[i]

for j in range(len(frecuencies_list)):
    summation_normalization += float(frecuencies_list[j]/summation_frecuencies)

print("==================== Data Normalization result =============================")
print(summation_normalization)