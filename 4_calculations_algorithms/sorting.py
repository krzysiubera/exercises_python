import random
import math
import numpy as np


def bubble_sort(numbers):
    swapped = True

    while swapped:
        swapped = False
        for idx in range(len(numbers) - 1):
            if numbers[idx] < numbers[idx + 1]:
                numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]
                swapped = True


if __name__ == '__main__':
    # generate numbers
    random_numbers = [random.random() for _ in range(50)]

    # sorted by function from standard library
    random_numbers_sorted_by_std_library = sorted(random_numbers, reverse=True)

    # sorted by bubble_sort() function
    bubble_sort(random_numbers)

    if np.allclose(random_numbers, random_numbers_sorted_by_std_library):
        print("Sorting went ok")
        print(f"Sorted numbers: {random_numbers}")
    else:
        print("Sorting went wrong")
