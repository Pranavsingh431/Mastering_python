#SCATTER GRAPH

x = [99, 90, 85, 97, 80]
y = [100, 85, 60, 90, 70]
plt.scatter(x, y, label = 'points')
plt.title('x vs y')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc= 9) # this means the legend will be in the center.
plt.axis('equal') # this equals the values of axis points as matplotlib can give us the graph with different x and y axis.
plt.show()
