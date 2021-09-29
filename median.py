#median
import numpy as np
from statistics import median_grouped
import grouped
#calcukate CF
def CF(freq):
    cf = [0]
    for a in freq:
        cf.append(a+cf[-1])
    cf.pop(0)
    return cf
#ungrouped

def median_freq(X,freqs,grouped=False):
    temp = []
    itr = 0
    for freq in freqs:
        temp+=([X[itr] for i in range(freq)])
        itr+=1
    cf= CF(freqs)
    data = np.array(temp)
    median = median_grouped(data)

    return(median)

def grp_median(low,up,h,freak):

    t = grouped.grouping(low, up,h)

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

    print("hola", MEDIAN)
