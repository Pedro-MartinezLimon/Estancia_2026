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

    # Exponents of T and dt
    A_parameter = int(input("A (1-4): "))
    B_parameter = int(input("B (1-3): "))

    # N = T ** (A)/dt ** (-B)
    #  = 10 ** (A)/ 10 ** (-B) 
    #  = 10 ** (A + B)

    for i in range(10 ** (A_parameter + B_parameter)):
        if(Birth(birth_rate, B_parameter)):
            
            total_proteins += 1
            time_proteins.append(total_proteins)
        
        if(total_proteins > 0):
            death_count = 0

            for j in range(total_proteins):
                if(Death(death_rate, B_parameter)):
                    death_count += 1

            total_proteins -= death_count
            time_proteins.append(total_proteins)

    print("========= Results (momentos (dt)) =============")
    print(time_proteins)