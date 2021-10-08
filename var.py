import numpy as np
from mean import *
from misc import *

def md(X,freq):
    X_hat = freq_mean(X,freq)['mean'] 
    mean_dev = np.sum(np.abs(freq*(X-X_hat)))/np.sum(freq)
    cd = mean_dev/X-hat
    info = {'cd of mean dev': cd,'mean dev':mean_dev,'X-X_hat':X-X_hat,'freq*(X-X_hat)':freq*(X-X_hat)}
    

def std_dev(X,freq):
    mean = freq_mean(X,freq)['mean']
    A = np.median(X)
    h = X[1]-X[0]
    D = (X - A)/ h
    fi_di= freq*D
    fi_di2 = freq*(D**2)
    n = np.sum(freq)
    std = np.sqrt(((h/n)**2)*((n*(np.sum(fi_di2)))-((np.sum(fi_di))**2)))
    cd = sd/mean
    info = {'D':D,'fi_di':fi_di,'sum_fi_di':np.sum(fi_di),'fi_di2':fi_di2,'sum_fi_di2':np.sum(fi_di2),'std':std}
    return info

    

def var(X,freq):
    return (std_dev(X,freq)['std'])**2