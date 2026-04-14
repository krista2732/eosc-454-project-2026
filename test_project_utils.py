import numpy as np
import project_utils as pu

# file for test cases!

test_dict = {1:{'iter':1, 'beta':1000, 'phi_d': np.float64(1.11), 'phi_m': np.float64(11.11)}, 
             2:{'iter':2, 'beta':2000, 'phi_d': np.float64(2.22), 'phi_m': np.float64(22.22)}}

test_betas = [1000, 2000]
test_phi_ds = [1.11, 2.22]
test_phi_ms = [11.11, 22.22]

betas, phi_ds, phi_ms

assert betas == test_beta