import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('example.txt', 'r') as csvfile:
    fileContents = csv.reader(csvfile, delimiter=',')
    for row in fileContents:
        x.append(int(row[0]))
        y.append(int(row[1]))
plt.plot(x, y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('My first plot\nwith matplotlib')
plt.show()
