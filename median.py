#median
import numpy as np
#ungrouped
def median(X):
    return np.median(X)
def median_freq(X,freqs):
    temp = []
    itr = 0
    for freq in freqs:
        temp+=([data[itr]for i in range(freq)])
        itr+=1
    data = np.array(temp)
    cf = [0]
    for a in freq:
        cf.append(a+cf[-1])
    cf.pop(0)
    median = np.median_grouped(data)
