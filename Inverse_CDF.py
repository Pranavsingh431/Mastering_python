#INVERSE NORMAL_CDF
#sometimes we need to find the value corresponding to the cdf, in that case we use inverse of normal_cdf using binary search.

import math
import matplotlib.pyplot as plt
def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    if mu != 0 and sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    
    low_z = -10.0
    high_z = 10.0
    while high_z - low_z > tolerance:
        mid_z = (high_z + low_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z = mid_z
        elif mid_p > p:
            high_z = mid_z
        else:
            break
    return mid_z
