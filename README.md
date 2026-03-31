# EIGENVALUES-AND-EIGENVECTORS
## Aim:
To write a python program to find the Eigenvalues and Eigen Vectors
## Equipment’s required:
1. 	Hardware – PCs
2. 	Anaconda – Python 3.7 Installation / Moodle-Code Runner
## Algorithm:
### Step1 : Import the numpy module to use the built-in functions for calculation
### Step 2: Prepare the lists from each linear equations and assign in np.array()
### Step 3: Using the np.linalg.eig(),  we get two results (first is eigenvalue and second is eigenvector) of the given matrix.
### Step 4: End the program



## Program:
#Program to find the eigen values and eigen vectors.
#Developed by: Vaishnavi S
#RegisterNumber:25011331
import numpy as np
import numpy as np

A = np.array([[-2,2,-3],[2,1,-6],[-1,-2,0]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigen values are", eigenvalues,"and Eigen Vectors are", eigenvectors)
## Output:
<img width="1224" height="806" alt="Screenshot 2026-02-10 114130" src="https://github.com/user-attachments/assets/0c328646-7ce4-43ec-920f-9baa423e1d9b" />

## Result:
Thus the Eigenvalue and Eigenvector is successfully solved using python program
