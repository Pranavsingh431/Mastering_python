#BAR GRAPH BUT COOLER

from collections import Counter
grades = [83, 95, 91,87,70,0,85,82,100,67,73,77,0]
'''It seems that if we are given only one list and we are told to plot a graph, then we can first convert that list into a 
dictionary like by using counter and then using the keys and values as x and y axis to plot the graph.'''

decile = lambda grade : grade//10 * 10 #it is used to change 83 to 80 and so on to make categories of marks.
h = Counter(decile(grade) for grade in grades) #if not used this way then each marks will be counted as 1 and the graph will be wrong.

plt.bar(h.keys(), h.values(), 8) #this 8 is the width of the bar.
plt.axis([-5, 105, 0, 5]) #specifying x and y axis range respectively.

plt.xticks([10*i for i in range(11)]) #to mark the x axis from 0 to 100.
plt.show()
