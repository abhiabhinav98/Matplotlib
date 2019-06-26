import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8]
y =[3,5,4,2,6,8,9,7]

plt.scatter(x,y,label='skitscat', color='k', marker='*', s=50)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interesting")

plt.show()