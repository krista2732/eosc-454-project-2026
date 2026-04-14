import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse as sp
import ipywidgets

# file for future functions!

def plot_tikhonov_curves(dictionary, target):
    # initalize arrays
    betas = []
    phi_ms = []
    phi_ds = []

    # get list of iterations done
    list_iterations = dictionary.keys()

    for i in list_iterations:
        betas.append(dictionary[i]['beta'])
        phi_ms.append(dictionary[i]['phi_m'])
        phi_ds.append(dictionary[i]['phi_d'])

    target_line = target.target

    fig, ax = plt.subplots(1, 3, figsize=(12, 4)) 
    
    ax[0].semilogx(betas, phi_ds)
    ax[1].semilogx(betas, phi_ms)
    ax[2].loglog(phi_ms, phi_ds) 

    # plot beta at the beta index
    ax[0].semilogx(betas, phi_ds, "ro")
    ax[1].semilogx(betas, phi_ms, "ro")
    ax[2].loglog(phi_ms, phi_ds, "ro")
    
    ax[0].set_ylabel(r"$\phi_d$")
    ax[1].set_ylabel(r"$\phi_m$")
    
    ax[2].set_xlabel(r"$\phi_m$")
    ax[2].set_ylabel(r"$\phi_d$")

    # add target misfit 
    ax[0].semilogx(betas, np.ones(len(betas))*target_line, "--k")
    ax[2].loglog(phi_ms, np.ones(len(phi_ms))*target_line, "--k")
     
    plt.tight_layout()
