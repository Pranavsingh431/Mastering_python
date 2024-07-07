#--------------------------#
#ORDER OF MATRIX
def shape(A):
    rows = len(A)
    columns = len(A[0]) if A else 0
    return rows, columns
