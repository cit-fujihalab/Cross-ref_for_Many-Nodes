import matplotlib.pyplot as plt

domain = [10, 18, 28, 38, 49, 61, 89, 105, 116]
peak = [35, 57, 100, 125, 155, 205, 300, 350, 390]
lower = [25, 45, 75, 110, 145, 200, 280, 330, 375]
upper = [65, 90, 140, 170, 185, 250, 350, 410, 455]

plt.plot(domain, peak, label="peak")
plt.plot(domain, lower, label="lower")
plt.plot(domain, upper, label="upper")
plt.xlabel("# of domains")
plt.ylabel("latency of cross referencing")
plt.legend()
#plt.show()
plt.savefig('domain_size-tendency.png')
