import numpy as np


A = [1, 2, 12, 4]
B = [2, 4, 2, 8]

if len(A) != len(B):
    raise RuntimeError("Dimensions of vectors don't match")

scalar_product = 0
for a, b in zip(A, B):
    scalar_product += a * b

if np.allclose(scalar_product, np.inner(A, B)):
    print("Correct result")
    print(f"Scalar product is: {scalar_product}")
else:
    print("Wrong result")
