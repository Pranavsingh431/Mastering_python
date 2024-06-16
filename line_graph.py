#using matplotlib library to plot a simple graphs.
import matplotlib.pyplot as plt

#--------------------------#
#LINE GRAPH
x = [1,2,3,4]
y = [2,4,6,8]
plt.plot(x,y, color= 'black', marker= 'o') #marker is used to mark the points where x and y are kindof plotted.
plt.title('x vs y')#it is used to give title to the graph.
plt.xlabel('x axis') #these are used to give labels to the x and y axis.
plt.ylabel('y axis')
plt.show()
