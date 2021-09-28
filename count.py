import numpy as np
def count(X,grouped=False):
    info = {}
    if grouped== False:
        uniques = np.unique(X)
        for unique in uniques:
            info[unique]=0
        for elem in X:
            info[elem]+=1
        return info
    elif grouped==True:
        pass