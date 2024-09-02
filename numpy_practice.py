# Temperature Conversion: Create a NumPy array of temperatures in Celsius: temps_celsius = np.array([0, 20, 35, 40]). Convert
#  this array to Fahrenheit using  the formula F = (C * 9/5) + 32 and print the Fahrenheit values.
import numpy as np
temps_celsius=np.array([0, 20, 35, 40])
temp_Fahrenheit=(temps_celsius*9/5)+32
print(temp_Fahrenheit)

#Finding Unique Elements: Create a 1D array with some duplicate elements: arr = np.array([1, 2, 2, 3, 4, 4, 5]).
# Find and print the unique elements of the array.
arr =np.array([1, 2, 2, 3, 4, 4, 5])
print(np.unique(arr))

#Transpose of a Matrix: Create a 3x3 matrix matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]). 
# Find and print its transpose.
matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix1.T)

# Handling Missing Data: Create an array arr = np.array([1, 2, np.nan, 4, 5]). 
# Calculate the mean of the array, ignoring the NaN values.
arr=np.array([1,2,np.nan,4,5])
mean = np.nanmean(arr)
print(mean)

#Finding the Closest Value: Given an array arr = np.array([10, 20, 30, 40, 50]) and a target value target = 33,
#find the element in the array that is closest to the target value.
arr=np.array([10,20,30,40,50])
target=33
closest_value= arr[np.abs(arr - target).argmin()]
print(closest_value)




