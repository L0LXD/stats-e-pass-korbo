'''
import numpy as np
lower = 30
upper = 100
class_interval = 5
lower_bd = np.arange(lower,upper,class_interval)
upper_bd = np.arange(lower_bd[1],upper+1,class_interval)
lower_bd,upper_bd, temp=[],[lower],lower
while temp<upper:
    lower_bd.append(upper_bd[-1])
    upper_bd.append(lower_bd[-1]+class_interval)
    temp+=class_interval
upper_bd.pop(0)

print(lower_bd,"\n",upper_bd)
mid_pts = (upper_bd + lower_bd)/2
print(mid_pts)
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
'''

dict = {"a":2,'b':2}
dict["a"]=dict['a']+1
print(dict)