#--------------------------#
#SUM OF SQUARES
def sum_of_squares(v):
    return dot_product(v,v)

#--------------------------#
#MAGNITUDE
import math
def magnitude(v):
    return math.sqrt(sum_of_squares(v))

#--------------------------#
#DISTANCE BETWEEN TWO VECTORS
def distance(v,w):
    return math.sqrt(sum_of_squares(vector_sub(v,w)))
