import numpy as np
import matplotlib.pylab as plt

data3 = np.genfromtxt("data3.dat")

datas = []
for i in range (len(data3)):
    if(data3[i]!=0):
        datas.append(data3[i])
        
plt.hist(np.log(datas),bins=20)
plt.savefig("hist3.png")

print("mean =",np.mean(datas))
print("standard deviation = ",np.std(datas))