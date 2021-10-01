import numpy as np
from math import log10
def struge(range_diff,n):
    #k = number of classes
    #range_diff = lowerst - highest 
    #n = Total frequecny
    #c = class intervel = range/k

    k = 1+(3.3222+log10(n))
    c = round(range_diff/k)
    #approxing
    temp = c%10
    if temp==5 or 0:
        pass
    elif temp<5:
        c = ((c//10)*10 )
    elif temp>5:
        c = ((c//10 +1)*10 )
    return c,k #returns class intervel and number of classes
def grouping(lower,upper,class_interval,inc=False):    
    lower_bd = np.arange(lower,upper,class_interval)
    upper_bd = np.arange(lower_bd[1],upper+1,class_interval)
    if inc ==True: 
        lower_bd = (lower_bd - 1)
        lower_bd[0]+=1
    mid_pts = (upper_bd + lower_bd)/2
    return lower_bd,upper_bd,mid_pts
def count(X,grouped=False,lower_bd=None,upper_bd=None,class_interval=None):
    info = {}
    if grouped== False:
        uniques = np.unique(X)
        for unique in uniques:
            info[unique]=0
        for elem in X:
            info[elem]+=1
        return info
    elif grouped==True:
        uniques = np.unique(X)
        np.sort(uniques)
        if lower_bd== None:
            lower_bd=(uniques[0]//10 )*10
        if upper_bd== None:
            upper_bd=((uniques[-1]+1)//10 )*10
        if class_interval==None:
            class_interval,k=struge((upper_bd-lower_bd),X.shape[0])
        
        
        lower_bd,upper_bd,mid_pt = grouping(lower_bd,upper_bd,class_interval)
        for unique in uniques:
            unique=int(unique)
            print(unique)
            for i in range(len(lower_bd)):
                if unique in range(int(lower_bd[i]),int(upper_bd[i])):
                    temp_range = '{}-{}'.format(lower_bd[i],upper_bd[i])
                    print(temp_range)
                    if temp_range not in info.keys():
                        info[temp_range]=0
                    info[temp_range]=info[temp_range]+1
        return info
       
