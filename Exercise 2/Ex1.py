import numpy as np
import random

t = 0
L = 100
si = 90
sv = 50
T = 300
rrec = 4
Niter = 0
Nitermax = 300
N = 600

def uL(z):
    if(z>0,z<=L):
        return 1/L
    else:
        return 0

def position(x,y,z):
    return (1/(2*np.pi*si*sv))*np.exp(-(x**2+y**2)/(2*si*sv))*uL(z)

positions_i = np.zeros((300,3))
positions_v = np.zeros((300,3))
for i in range(0,300):
    rx_i = random.random()*100
    ry_i = random.random()*100
    rz_i = random.random()*100
    positions_i[i,0],positions_i[i,1],positions_i[i,2] = rx_i,ry_i,rz_i
    rx_v = random.random()*100
    ry_v = random.random()*100
    rz_v = random.random()*100
    positions_v[i,0],positions_v[i,1],positions_v[i,2] = rx_v,ry_v,rz_v
    
new_positions_i = []
new_positions_v = []
for i in range(0,int(N/2)):
    for j in range(0,int(N/2)):
        if(np.sqrt((positions_i[i,0]-positions_v[i,0])**2 + (positions_i[i,1]-positions_v[i,1])**2 + (positions_i[i,2]-positions_v[i,2])**2) < rrec):
            np.delete(positions_i,[])
            N -= 2
            
Kb = 8.617332478*pow(10,-5)
wi = 1.717*(10**15)
wv = 0.001282*(10**15)
Bi = 1.37
Bv = 0.1
def T(w,B,T):
    return w*np.exp(-B/(Kb*T))

while(t<=10**(-6)):
    lista = [T(wi,Bi,300),T(wv,Bv,300)]

    R = np.sum(lista)

    Rlista = []
    suma = 0
    for i in range(len(lista)):
        suma += lista[i
        Rlista.append(suma)

    u = random.random()

    for i in range (len(Rlista):

        
    u4 = random.random()
    t += (-np.log(u4)/R)
