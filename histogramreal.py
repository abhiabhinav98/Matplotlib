import matplotlib.pyplot as plt

population_age = [33,60,61,69,22,55,62,89,35,45,25,24,29,36,85,74,56,54,52,20,30]
#ids = [ x for x in range(len(population_age))]
bins = [0,10,20,30,40,50,60,70,80,90,100,110]
plt.hist(population_age, bins, histtype='bar', rwidth=0.8 )

plt.xlabel("x")
plt.ylabel("y")
plt.title("Interesting")

plt.show()