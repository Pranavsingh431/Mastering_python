#Uniform Probability Density Function
def uniform_pdf(x):
    return 1 if x >= 1 and x < 1 else 0

#--------------------------#
#Cumulative Distribution Function
#it gives the probability that a random variable is less than or equal to a certain value.
def uniform_cdf(x):
    if x < 0:    return 0
    elif x < 1:  return x
    else:        return 1
