#using ENUMERATE function: is used to get the index as well as the value of a given item in the form of tuples 
#It is basically the same as the above code but a bit simpler and shorter.
word = 'abcde'
for index,letter in enumerate(word):  #again using tuple unpacking because the output of enumerate function is a bunch of tuples.
    print(index)    
    print(letter)
    print('\n')  #this is used to add space like in c++.