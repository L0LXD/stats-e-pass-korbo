import numpy as np
import mean as m
from median import *
X = np.array([47.5,52.5,57.5,62.5,67.5,72.5,77.5])
freq = np.array([5,8,30,25,14,12,6])
A = np.median(X)
'''sed = m.range_mean(X,freq,A)
print(sed['A'],sed['D'],sed['freq'],sed['FD'])
print(sed['mean'])
m.step_deviation(X,freq,62.5)'''
X =  np.array([25,20,15,35,8])
print(median_freq(2,X))
