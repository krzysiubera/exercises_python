import numpy as np
import random
import copy


def smaller_matrix(bigger_matrix, row, col):
    # we don't want to affect the original matrix
    new_matrix = copy.deepcopy(bigger_matrix)

    # removing rows
    new_matrix.remove(bigger_matrix[row])

    # removing columns
    for idx in range(len(new_matrix)):
        new_matrix[idx].pop(col)

    return new_matrix


def get_determinant(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    if n_rows != n_cols:
        raise ValueError("It is impossible to calculate a determinant from that matrix")

    # base case
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        det = 0
        # iterate over rows
        for idx in range(n_cols):
            det += ((-1) ** idx) * matrix[0][idx] * get_determinant(smaller_matrix(matrix, 0, idx))
        return det


if __name__ == '__main__':
    dim_of_matrix = np.random.randint(1, 5)
    A = [[random.random() for _ in range(dim_of_matrix)] for _ in range(dim_of_matrix)]
    print(f"The matrix has size {dim_of_matrix}x{dim_of_matrix}")
    det_A = get_determinant(A)
    if np.allclose(det_A, np.linalg.det(A)):
        print(f"Correct result: {det_A}")
    else:
        print("Wrong result")
