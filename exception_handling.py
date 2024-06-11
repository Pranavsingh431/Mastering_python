#----------------------------------
#EXCEPTION HANDLING
#in python there are some instances where there are some exceptions and to handle those exceptions we use exception handling.
try:
    print(2/0) #we know this will give some error.
except:
    print("division with 0 does not exist.") #so instead of an error,  we give a condtion that instead of the above code run this error line.
finally:
    print("this is something differnt like this statement will run no matter the above output as it is final.")