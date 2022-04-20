import matplotlib.pyplot as plt
import numpy as np

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

dico = parse("square-3-1.txt")
D = {
    "m3-5" :[4.00,8.00,1.20],
    "m3-6" :[4.00,8.00,2.10],
    "m3-7" :[6.00,8.00,1.20],
    "m3-8" :[6.00,8.00,2.10],
    "m3-9" :[8.00,8.00,1.20],
    "m3-10":[8.00,8.00,2.10],
    "m3-21":[4.00,6.00,1.20],
    "m3-22":[4.00,6.00,2.10],
    "m3-23":[8.00,6.00,1.20],
    "m3-24":[8.00,6.00,2.10],
    "m3-33":[4.00,4.00,1.20],
    "m3-34":[4.00,4.00,2.10],
    "m3-35":[6.00,4.00,1.20],
    "m3-36":[6.00,4.00,2.10],
    "m3-37":[8.00,4.00,1.20],
    "m3-38":[8.00,4.00,2.10]
}
P = {
    "m3-5" :[0, 0],
    "m3-6" :[0, 0],
    "m3-7" :[0, 0],
    "m3-8" :[0, 0],
    "m3-9" :[0, 0],
    "m3-10":[0, 0],
    "m3-21":[0, 0],
    "m3-22":[0, 0],
    "m3-23":[0, 0],
    "m3-24":[0, 0],
    "m3-33":[0, 0],
    "m3-34":[0, 0],
    "m3-35":[0, 0],
    "m3-36":[0, 0],
    "m3-37":[0, 0],
    "m3-38":[0, 0]
}
for cle,val in P.items():
    for c,v in dico.items():
        if cle == v[1] :
            val[1]+=1
            if v[2] != "":
                val[0]+=1

print(P)







fig = plt.figure()
ax = fig.add_subplot(projection='3d')
color_map = plt.get_cmap('plasma')

n = 100
X = list()
Y = list()
Z = list()
c = list()
for cle, val in D.items():
    X.append(val[0])
    Y.append(val[1])
    Z.append(val[2])
    if (P[cle][1]==0):
        c.append(0.0)
    else:
        c.append(P[cle][0]/P[cle][1])




scatter_plot=ax.scatter(X, Y, Z, c=c, cmap = color_map, s=100)
plt.colorbar(scatter_plot)
ax.set_xlabel('X ')
ax.set_ylabel('Y ')
ax.set_zlabel('Z ')
plt.title("Delivery ratio")
plt.savefig("pdr-3-1.png")

plt.show()