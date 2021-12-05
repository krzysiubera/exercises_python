import concurrent.futures
import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def roll_the_dice():
    """
    Simulation of rolling the dice
    :return: random int between 1 and 6
    """
    return random.randint(1, 6)


def calculate_histogram(num_runs=100_000):
    """
    Simulation of rolling the dice num_runs times and adding result from first and second dice
    :param num_runs: how many times we should simulate rolling the dice
    :return: x_axis and y_axis to be plotted
    """

    dice_rolls = np.zeros(num_runs, dtype=int)
    for idx in range(num_runs):
        dice_rolls[idx] = roll_the_dice() + roll_the_dice()

    cnt = Counter()
    for result in dice_rolls:
        cnt[result] = cnt[result] + 1

    sorted_cnt = {k: v for k, v in sorted(list(cnt.items()))}

    x_axis = list(sorted_cnt.keys())
    y_axis = list(sorted_cnt.values())

    return x_axis, y_axis


def run_calc():
    """
    Running threads and showing results
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as thread:
        th = thread.submit(calculate_histogram, 100_000)

    x_axis, y_axis = th.result()

    fig, ax = plt.subplots()
    ax.stem(x_axis, y_axis, use_line_collection=True)
    ax.set_title("Simulation of rolling two dices")
    plt.show()


if __name__ == '__main__':
    run_calc()