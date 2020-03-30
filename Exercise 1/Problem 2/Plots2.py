import numpy as np
import matplotlib.pylab as plt

data2 = np.genfromtxt("data2.dat", delimiter=",")

plt.figure(figsize=(17,8))

plt.subplot(2,3,1)
plt.errorbar(data2[:7,0],data2[:7,1],marker=".")
plt.title("l1 = 1, l2 = 2")
plt.xlabel("N")
plt.ylabel("<r2>")
plt.grid()

plt.subplot(2,3,2)
plt.errorbar(data2[7:14,0],data2[7:14,1],marker=".")
plt.title("l1 = 2, l2 = 3")
plt.xlabel("N")
plt.ylabel("<r2>")
plt.grid()

plt.subplot(2,3,3)
plt.errorbar(data2[14:21,0],data2[14:21,1],marker=".")
plt.title("l1 = 3, l2 = 4")
plt.xlabel("N")
plt.ylabel("<r2>")
plt.grid()

plt.subplot(2,3,4)
plt.errorbar(data2[21:28,0],data2[21:28,1],marker=".")
plt.title("l1 = 4, l2 = 5")
plt.xlabel("N")
plt.ylabel("<r2>")
plt.grid()

plt.subplot(2,3,5)
plt.errorbar(data2[28:,0],data2[28:,1],marker=".")
plt.title("l1 = 5, l2 = 6")
plt.xlabel("N")
plt.ylabel("<r2>")
plt.grid()

plt.subplots_adjust(hspace=.3)
plt.savefig("plots2.png")