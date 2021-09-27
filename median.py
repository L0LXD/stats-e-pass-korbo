#median
import numpy as np
#ungrouped
def median(X):
    return np.median(X)
#grouped
def median_freq(X,freqs):
    data = []
    for freq in freqs:
        data =[X[temp]for i in freq]
        temp+=1
    median = np.median_grouped(data)
    cf = [0]
    for a in freq:
        cf.append(a+cf[-1])
    cf.pop(0)
        