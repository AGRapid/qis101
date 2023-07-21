#!/usr/bin/env python3
"""benfords_law.py"""

# In sets that obey the law, the number 1 appears as the leading significant digit about
# 30% of the time, while 9 appears as the least significant digit less than 5%.
# https://en.wikipedia.org/wiki/Benford%27s_law

# Referenced Chat GPT for help in obtaining and storing the significant digits

import matplotlib.pyplot as plt
import numpy as np

from random import randint

from matplotlib.axes import Axes


def plot(ax: Axes) -> None:
    """This function will find random digits, calculate the probability of the
    significant digit, and plot a histogram of the probabilities of each digit"""

    # d is for digits from 1 to 9 inclusive
    d = list(range(1, 10))

    # The probability of the leading digit is given by the following formula
    # To the 100th power.
    random_int: list[int] = [
        np.power(randint(1, 1_000_000), 100) for _ in range(100_000)
    ]

    # The significant digits are obtained from the random draw
    sig_dig: list[int] = [int(str(abs(_))[0]) for _ in random_int]

    # Each value is stored in a list
    val: list[int] = [sig_dig.count(x) for x in d]

    # Summing all values
    total_counts: int = sum(val)

    # The probability is the index value/ total index value
    probability: list[float] = [y / total_counts for y in val]

    # Plotting the histogram
    plt.bar(d, probability, color="orange")
    ax.set_title("Benford's Law")
    ax.set_xlabel("Significant Digits")
    ax.set_ylabel("Probability of Digits")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
