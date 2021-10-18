import numpy as np
import random


dim_of_matrix = 8
A = [[random.random() for _ in range(dim_of_matrix)] for _ in range(dim_of_matrix)]
B = [[random.random() for _ in range(dim_of_matrix)] for _ in range(dim_of_matrix)]
result = [[0 for _ in range(dim_of_matrix)] for _ in range(dim_of_matrix)]

rows_A = len(A)
cols_A = len(A[0])
rows_B = len(B)
cols_B = len(B[0])

for i in range(rows_A):
    for j in range(cols_B):
        for k in range(rows_B):
            result[i][j] += A[i][k] * B[k][j]

# check if result is ok
if np.allclose(result, np.array(A) @ np.array(B)):
    print(f"Correct result")
else:
    print("Wrong result")
