import random
import numpy as np


dim_of_matrix = 128
A = [[random.random() for _ in range(dim_of_matrix)] for _ in range(dim_of_matrix)]
B = [[random.random() for _ in range(dim_of_matrix)] for _ in range(dim_of_matrix)]

result = [[A[i][j] + B[i][j] for j in range(dim_of_matrix)] for i in range(dim_of_matrix)]

if np.allclose(result, np.add(A, B)):
    print("Correct result")
else:
    print("Wrong result")
