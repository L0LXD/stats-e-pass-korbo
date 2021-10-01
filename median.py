import numpy as np
from misc import grouping
#calcukate CF
def CF(freq):    
    cf = [0]
    for a in freq:
        cf.append(a+cf[-1])
    cf.pop(0)
    return cf
def median(X,freqency=[]):
    #if frequency is not included frequency for each ele will be calculated
    temp =[]
    if freqency==[]:
        freqs = [1 for ele in X]
    else:
        freqs = freqency
    print(freqs)
    itr = 0
    for freq in freqs:
        temp+=([X[itr] for i in range(freq)])
        itr+=1
    cf= CF(freqs)
    data = np.array(temp)
    median = np.median(data)
    return data,median
def grp_median(low,up,h,freak,inclusive=False):

    t = grouping(low, up,h,inc = inclusive)

    median_term = 0

    lower_bounds = t[0]
    upper_bounds = t[1]
    frequency = freak
    cf_of_frequency = CF(frequency)
    print("len of cf list: ", len(cf_of_frequency))
    print("cf: ", cf_of_frequency)
    if cf_of_frequency[-1]%2 == 0:
        N = (cf_of_frequency[-1])/2
    else:
        N = (cf_of_frequency[-1] + 1)/2
    
    print("N: ", N)

    for i in range(0,len(cf_of_frequency)):
        if N <= cf_of_frequency[i]:
            median_term += i
            break

    print("median_term: ", median_term)
    print("cf of median class",cf_of_frequency[median_term])

    height = t[1][median_term] - t[0][median_term]

    print("height", height)

    print(t[0][median_term])

    MEDIAN = t[0][median_term] + ((N - cf_of_frequency[(median_term)-1])/frequency[i])*height

    print(MEDIAN)
X = np.array([2,4,6,7])
freqs = np.array([5,20,35,7,3])
grp_median(0,100,20,freqs)