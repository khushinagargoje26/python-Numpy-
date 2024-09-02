import numpy as np 
#creating a 1d array 
# arr=np.array([1,3,4,5,6,7,5])
# print(arr)

# #creating 2d array 
# arr2=np.array([[1,2,3],[4,5,6]])
# print(arr2)

# #for properties 
# print(arr.ndim)
# print(arr2.shape)
# print(arr.size)
# print(arr2.shape)
# print(arr.dtype)
# print(arr2.dtype)

#Baic array operations 
# arr1=np.array([3,4,5])
# arr2=np.array([6,7,8])
# result=arr1+arr2
# print(result)


# result=arr1*arr2
# print(result)

# result=arr1-arr2
# print(result)
# result=arr1/arr2
# print(result)
#Scalar operations
# result=arr1*2
# print(result)
# arr=np.array([1,3,5,7,8,8,8])
# arr2d=np.array([[2,3,4],[2,8,9],[4,3,5]])
# print(arr2d[0,1:])
# print(arr2d[1:,1:])#slicing
#finding min max mean sum of array
arr=np.array([2,5,6,7,8,0])
print(np.mean(arr))
print(np.sum(arr))
print(np.max(arr))
print(np.min(arr))

#Finding the indes of max and min array
print(np.argmax(arr))
print(np.argmin(arr))
#Reshaping Arrays
reshape_arr=arr.reshape(2,3)
print(reshape_arr)
#Matrix Operations 
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[6,7],[8,9]])
#Matrix Multiplications
result=np.dot(arr1,arr2)
print(result)
#Transpose of Matrix
print(arr1.T)

#Inverse of Matrix
result2=np.linalg.inv(arr1)
print(result2)


#Advance Array Creation 
Zero_array=np.zeros((2,3))
print(Zero_array)
ones_array=np.ones((3,2))
print(ones_array)





