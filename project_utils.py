import numpy as np

def kernel_function(x_nodes, kernel_index, exponent, oscillation): 
    """
    Function that provides decaying, oscillating kernels given 1D mesh nodes, x
    
    Parameters
    ----------
    x_nodes: numpy.ndarray
        mesh node locations

    kernel_index: int
        variable that indexes kernels

    exponent: float
        decay rate (if negative) or grwoth rate (if positive)

    oscillation: float
        how oscillatory our function is
    """
    return (
        np.exp(kernel_index*exponent*x_nodes) * 
        np.cos(2*np.pi*kernel_index*oscillation*x_nodes)
    )
