import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse as sp
import ipywidgets

# file for future functions!

def plot_tikhonov_curves(dictionary, target):
    '''
    Plots Tikhonov curves using output dictionary defining results for each iteration.
    
    '''
    # initalize arrays
    betas = []
    phi_ms = []
    phi_ds = []

    # get list of iterations done
    # sort entries by beta (largest to smallest)
    list_iterations = sorted(dictionary.keys())
    print(list_iterations)

    for i in list_iterations:
        betas.append(dictionary[i]['beta'])
        phi_ms.append(dictionary[i]['phi_m'])
        phi_ds.append(dictionary[i]['phi_d'])

    target_line = target.target

    fig, ax = plt.subplots(3, 1, figsize=(6, 13)) 

    # plot beta at the beta index
    ax[0].loglog(betas, phi_ds, color="blue")
    ax[0].invert_xaxis() # put betas in descending order
    ax[1].loglog(betas, phi_ms, color="blue")
    ax[1].invert_xaxis()
    ax[2].loglog(phi_ms, phi_ds, color="blue")
    
    ax[0].set_xlabel(r"$\beta$")
    ax[0].set_ylabel(r"$\phi_d$")

    ax[1].set_xlabel(r"$\beta$")
    ax[1].set_ylabel(r"$\phi_m$")
    
    ax[2].set_xlabel(r"$\phi_m$")
    ax[2].set_ylabel(r"$\phi_d$")

    # add target misfit 
    ax[0].loglog(betas, np.ones(len(betas))*target_line, color="red", linestyle="--", label=fr"Target Misfit: $\phi_d$ = {target_line:.0f}")
    ax[0].legend()
    ax[2].loglog(phi_ms, np.ones(len(phi_ms))*target_line, color="red", linestyle="--", label=fr"Target Misfit: $\phi_d$ = {target_line:.0f}")
    ax[2].legend()
     
    plt.tight_layout()
    plt.show()
