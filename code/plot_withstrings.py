import matplotlib.pyplot as plt


x = ['abc','bbb','ccc']
y = [11,22,33]


plt.plot(x, y, label='My plot!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.show()

# load data from a fi