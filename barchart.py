import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y=[6,7,8,2,4]
a =[1,3,5,7,9]
b= [5,6,9,1,2]

plt.bar(x,y, label='bar1', color='blue')
plt.bar(a,b, label ='bar2', color='c')
plt.xlabel("Plot number")
plt.ylabel("Important var")
plt.title("Interesting")
plt.legend()
plt.show()