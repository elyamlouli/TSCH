import matplotlib.pyplot as plt
import numpy as np
import math

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

dico = parse("square-10-1.txt")
print(dico)
L = list()
for cle,val in dico.items():
    if val[2] != "":
        i = val[2]-val[0]
        L.append(i)
L.sort()
m = np.average(L)
variance = np.var(L)
print("moyenne = ", m,"variance = ", variance)

n = len(L)
range = np.linspace(L[0], L[n-1], int(math.sqrt(n))+1)
plt.style.use('ggplot')
plt.hist(L, bins=range)
plt.title("Histogramme des délais des messages reçus")
plt.xlabel('Délais (s)')
plt.ylabel("Nombre d'occurrences")
plt.show()
plt.savefig("occ-10-1.png")






