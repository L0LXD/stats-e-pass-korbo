# dispersion
import numpy as np
from mean import *
from misc import *
def md(X,freq):
    X_hat = freq_mean(X,freq)['mean'] 
    mean_dev = np.sum(np.abs(freq*(X-X_hat)))/np.sum(freq)
    return mean_dev


def std_dev(X,freq):
    A = np.median(X)
    h = X[1]-X[0]
    D = (X - A)/ h
    fi_di= freq*D
    fi_di2 = freq*(D**2)
    n = np.sum(freq)
    std = np.sqrt(((h/n)**2)*((n*(np.sum(fi_di2)))-((np.sum(fi_di))**2)))
    return n,D,fi_di,np.sum(fi_di),fi_di2,np.sum(fi_di2),std
        
def var(X,freq):
    return (std_dev(X,freq))**2