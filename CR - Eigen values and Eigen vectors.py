#Program to find the eigen values and eigen vectors.
#Developed by: Vaishnavi S
#RegisterNumber:25011331
import numpy as np
import numpy as np

A = np.array([[-2,2,-3],[2,1,-6],[-1,-2,0]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigen values are", eigenvalues,"and Eigen Vectors are", eigenvectors)
