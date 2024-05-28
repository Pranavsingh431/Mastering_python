#some keywords that are useful while using loops.

#BREAK : ends the code totally when it occurs.
#but it is most likely used in case of while loops to stop the infinite iteration sometimes or any other condtion.
x = 'pranav'
for i in x:
    if i == 'a':
        break #it breaks the loop as soon as the given if condition is met.
    print(i)
    
#CONTINUE : like when it is used inside a loop, it goes ahead leaving the condtion where it is used and goes back to the loop and continues its task like if we want to leave something that we don't want to print.
x = 'pranav'
for i in x:
    if i == 'a':
        continue  #like here we don't want to print the letter 'a' so it is neglected and the loop continues to perform its operation.
    print(i)
    
#PASS : does nothing at all in case we don't want to do anything inside the loop.
x = [1,2,3,43,4]
for i in x:
    pass  #used like a filler here  