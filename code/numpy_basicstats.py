# axis-wise max min

import numpy as np 
a = np.array([[3,7,5],[8,4,3],[2,4,9]]) 

print (np.amin(a,1)) 
print (np.amin(a,0)) 
print (np.amax(a,1)) 
print (np.amax(a,1)) 


# Python Program illustrating  
# numpy.ptp() method  
    
    
# 1D array  
arr = [1, 2, 7, 20, np.NaN] 
print("arr : ", arr)  
print("Range of arr : ")
np.ptp(arr) 
  
#1D array  
arr = [1, 2, 7, 10, 16] 
print("arr : ", arr)  
print("Range of arr : ", np.ptp(arr)) 
