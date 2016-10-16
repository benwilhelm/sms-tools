from math import ceil
import numpy as np
from scipy.ndimage.interpolation import shift

def zeroPhaseWindow(x):
    zpw = np.zeros( len(x) )
    i = int(ceil(len(x) / 2.))
    j = i if (i == len(x)/2) else i - 1
    zpw[:i] = x[j:]
    zpw[i:] = x[:j]
    return zpw

def isEvenFunction(x, tolerance=0):
    if (len(x) % 2):
        x = x[1:]
    
    i = 0;
    while i < len(x)/2:
        j = -i - 1
        if (x[i] - x[j] > tolerance):
            return False 
        i += 1
    
    return True
    
