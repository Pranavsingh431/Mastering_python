#VECTOR ADDITION

def vector_sum(v, w):
    return [i+j for i,j in zip(v,w)] #this is somewhat similar to tuple unpacking as we are converting the vectors into a tuples.

#--------------------------#
#VECTOR SUBTRACTION

def vector_sub(v,w):
    return [i-j for i,j in zip(v,w)]

#--------------------------#
#SCALAR MULTIPLICATION

def scalar_multiply(v, c):
    return [c*i for i in v]
