#it can zips two or more lists together in the form of tuples which we can access using tuple unpacking afterwards.
l1 = [1,2,3]
l2 = ['a','b','c']
#we can use as many lists we want here.
print(list(zip(l1,l2)))#here we have converted the tuples in a single list.

####################
for i in zip(l1,l2):
    print(i) #now here we can use tuple unpacking to access the particulars elements from the tuples which are in the ouput.
