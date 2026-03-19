import numpy as np
from project_utils import kernel_function

# test length of kernel function
def test_length_kernels():
    n_nodes = 100
    x_nodes = np.linspace(0, 1, n_nodes)

    kernel = kernel_function(x_nodes, 1, 1, 1)
    passed = len(kernel) == n_nodes # T or F
    print(f"n_nodes: {n_nodes}, len(kernel): {len(kernel)}, passed?: {passed}")

    assert(len(kernel) == n_nodes)

# test when exponent equals zero
def test_exponent_zero():
    n_nodes = 100
    x_nodes = np.linspace(0, 1, n_nodes)
    kernel_index = 1
    exponent = 0
    oscillation = 2

    kernel = kernel_function(x_nodes, kernel_index=kernel_index, exponent=exponent, oscillation=oscillation)
    test_kernel = np.cos(2*np.pi*kernel_index*oscillation*x_nodes)

    # must account for numerical errors (make threshold)
    passed = np.allclose(kernel, test_kernel)

    print(f"kernel max: {np.max(kernel)}, test_kernel max: {np.max(test_kernel)}")
    print(f"kernel min: {np.min(kernel)}, test_kernel min: {np.min(test_kernel)}")
    print(f"kernel norm: {np.linalg.norm(kernel)}, test_kernel norm: {np.linalg.norm(test_kernel)}")
    assert(passed)

