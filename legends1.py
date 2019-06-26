import matplotlib.pyplot as plt

x = [1,2,3]
y=[7,8,6]
a = [12,22,16]
b = [9,7,8]
plt.plot(x,y, label = 'First line')
plt.plot(a,b, label= 'second line')
plt.xlabel("Plot number")
plt.ylabel("Important var")
plt.title("Interesting")
plt.legend()
plt.show()