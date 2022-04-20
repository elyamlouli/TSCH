
import matplotlib.pyplot as plt
import numpy as np
import math
NBR_NOEUD = 15
PAYLOAD_SIZE = 64*8 #bps

def parse (fichier):
    dico = {}
    with open(fichier, "r") as f:
        line = f.readline()
        
        while line != "":
            val = line.split(";")
            time = float(val[0])
            noeud = val[1]
            id_l = val[2].split(" ")
            key = id_l[1].strip('\n')
            if id_l[0] == "TX":
                l = [time, noeud, "", -1.0]
                dico[key] = l
            elif id_l[0] == "RX":
                if key in dico:
                    l = dico[key]
                    l[2] = time
                    l[3] = noeud
                    dico[key] = l
            line = f.readline()
    
    return dico




def mean_sigma(file):
    dico = parse(file)
    L = list()
    for cle,val in dico.items():
        if val[2] != "":
            i = val[2]-val[0]
            L.append(i)
    L.sort()
    m = np.average(L)
    variance = np.var(L)
    sigma = math.sqrt(variance)
   
    return (m, sigma)


L = ["square-1-1.txt", "square-3-1.txt", "square-5-1.txt", "square-7-1.txt", "square-10-1.txt"]
T = [1, 3, 5, 7, 10] 
trafic_load = list()
ecartype = list()
mean = list()
for i in range (len(T)):
    trafic_load.append(NBR_NOEUD*PAYLOAD_SIZE/T[i])
    m, sigma = mean_sigma(L[i])
    ecartype.append(sigma)
    mean.append(m)

print(ecartype, mean, trafic_load)
plt.title("Délai moyen par rapport à la charge de trafic")
plt.xlabel("Charge de traffic (bps)")
plt.ylabel("Délai (s)")
plt.errorbar(trafic_load, mean, ecartype)
plt.show()
plt.savefig("delai/charge.png")


