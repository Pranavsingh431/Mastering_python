#VECTOR MEAN
def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(vector_addition, 1/n)
