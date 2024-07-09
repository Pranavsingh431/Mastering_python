#CREATING A MATRIX
def matrix(number_of_rows, number_of_columns, entry_func):
    return [[entry_func(i, j)
            for j in range(number_of_columns)]
            for i in range(number_of_rows)]
