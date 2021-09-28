import numpy as np
def grouping(lower,upper,class_interval,inc=False):    
    lower_bd = np.arange(lower,upper,class_interval)
    upper_bd = np.arange(lower_bd[1],upper+1,class_interval)
    if inc ==True: 
        lower_bd = (lower_bd - 1)
        lower_bd[0]+=1
    mid_pts = (upper_bd + lower_bd)/2
    return lower_bd,upper_bd,mid_pts
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
