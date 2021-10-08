import numpy as np
from misc import grouping
#ungrouped mean
def no_freq_mean(X):
    np.mean(X)
    
# mean when frequency given
def freq_mean(X,freq):    
    XF = X*freq
    mean = np.sum(XF)/np.sum(freq)
    info = {'freq':freq,'mean':mean,"XF":XF}
    return info

#shortcut mean
def range_mean(X,freq,A =None):
    if A== None: A = np.median(X)
    D =X - A
    FD = D * freq
    mean =  float(A)+float(np.sum(FD))/np.sum(freq)
    info = {'A':A,'freq':freq,'D':D,'FD':FD,'mean':mean}
    return info

#weighted mean
def weighted_mean(X,weights):
    WX = X * weights
    mean = np.sum(WX)/np.sum(weights)
    info = {'weights':weights,'mean':mean,"WX":WX}
    return info

#step deviation
def step_deviation(X,freq,A = None):
    if A== None: A = np.median(X) 
    h = X[1]-X[0]
    U = (X - A)/h
    FU_fr = freq*U
    sum_FU = np.sum(FU_fr)
    sum_freq= np.sum(freq)
    mean = A + h * sum_FU/sum_freq
    info = {'X':X,'F':freq,'A':A,'U = (X - A)/h':U,'F*U':FU_fr,'mean':mean}
    return info       