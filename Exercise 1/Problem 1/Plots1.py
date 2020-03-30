import numpy as np
import matplotlib.pylab as plt

data = np.genfromtxt("data.dat", delimiter=",")

plt.figure(figsize=(16,3))

plt.subplot(1,3,1)
plt.plot(data[:10,0],data[:10,1],marker=".")
plt.title("M = 10")
plt.xlabel("N")
plt.ylabel("<r2>")
plt.grid()

plt.subplot(1,3,2)
plt.plot(data[10:20,0],data[10:20,1],marker=".")
plt.title("M = 100")
plt.xlabel("N")
plt.ylabel("<r2>")
plt.grid()

plt.subplot(1,3,3)
plt.plot(data[20:30,0],data[20:30,1],marker=".")
plt.title("M = 1000")
plt.xlabel("N")
plt.ylabel("<r2>")
plt.grid()

plt.savefig("plot1.png")

plt.figure(figsize=(17,8))

plt.subplot(2,3,1)
plt.errorbar(data[:10,0],data[:10,1],yerr=90.59899999999999,marker=".")
plt.title("M = 10")
plt.xlabel("N")
plt.ylabel("<r2>")
plt.grid()

plt.subplot(2,3,2)
plt.errorbar(data[10:20,0],data[10:20,1],yerr=29.204155555555555,marker=".")
plt.title("M = 100")
plt.xlabel("N")
plt.ylabel("<r2>")
plt.grid()

plt.subplot(2,3,3)
plt.errorbar(data[20:30,0],data[20:30,1],yerr=9.350215555555558,marker=".")
plt.title("M = 1000")
plt.xlabel("N")
plt.ylabel("<r2>")
plt.grid()

plt.subplot(2,3,4)
plt.errorbar(data[30:40,0],data[30:40,1],yerr=2.7313329,marker=".")
plt.title("M = 10000")
plt.xlabel("N")
plt.ylabel("<r2>")
plt.grid()

plt.subplot(2,3,5)
plt.errorbar(data[40:,0],data[40:,1],yerr=0.8625012999999999,marker=".")
plt.title("M = 100000")
plt.xlabel("N")
plt.ylabel("<r2>")
plt.grid()

plt.subplots_adjust(hspace=.3)
plt.savefig("plot1-1.png")