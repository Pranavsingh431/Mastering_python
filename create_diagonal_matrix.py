#CREATING A MATRIX
def matrix(number_of_rows, number_of_columns, entry_func):
    return [[entry_func(i, j)
            for j in range(number_of_columns)]
            for i in range(number_of_rows)]


#--------------------------#
#CREATING A DIAGONAL MATRIX
#firstly we will use the same above code to construct the matrix but now we will specify what is entry_func.
def diagonal(i,j):
    return 1 if i == j else 0
print(matrix(3,3,diagonal))
