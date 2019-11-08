# This function is used to calculate the Empirical Cumulative Distribution Function
# From datacamp Statistical thinking part 1
import numpy as np
def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    x = np.sort(data)
    y = np.arange(1, len(data)+1)/len(data) # make y stay in the range of (0,1)
    return x,y
