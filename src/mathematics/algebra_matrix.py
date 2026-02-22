#==============================================================================
# MATRIX
# - Multiply
# - Eigenvector/Eigenvalue
#==============================================================================
import numpy as np

mat_a = np.matrix([[1, 2], [3, 4], [5, 6]])
mat_b = np.matrix([[1], [1]])

mat_ret = np.matmul(mat_a, mat_b)

print(f"Shape of matrix: {mat_a.shape}")
print(f"Result is {mat_ret} with shape: {mat_ret.shape}")

a = np.matrix([[2, 1], [1, 2]])
eigenvalues, eigenvectors = np.linalg.eig(a)
print(f"eigenvalues: {eigenvalues}\neigenvectors: {eigenvectors}")
