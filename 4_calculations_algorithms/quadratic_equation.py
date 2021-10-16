import sys
import math

"""
Note: coefficients of the quadratic equation should be passed from command line
"""


if len(sys.argv) != 4:
    print("Wrong number of parameters provided")
else:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    except ValueError:
        raise RuntimeError("Wrong parameters provided")

    if math.isclose(a, 0.0):
        raise RuntimeError("Not a quadratic equation")

    try:
        delta = math.sqrt((b ** 2) - (4 * a * c))
    except ValueError:
        raise RuntimeError("Delta is less than 0")

    x1 = (-b - delta) / (2 * a)
    x2 = (-b + delta) / (2 * a)

    if math.isclose(x1, x2):
        print(f"Result is x = {x1}")
    else:
        print(f"Results are x1 = {x1}, x2 = {x2}")
