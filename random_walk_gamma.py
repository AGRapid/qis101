#!/usr/bin/env python3
"""random_walk_gamma.py"""

from __future__ import annotations


# Euler's Gamma function referred to from
# https://docs.python.org/2/library/math.html#special-functions
# from math import gamma
# Turns out math.gamma does not work with numpy arrays, use scipy.special.gamma instead


import typing
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma  # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def exp_dist(dims: NDArray[np.float_], num_steps: int):  # type: ignore
    """This function will calculate the expected final distance of a uniform
    random walk of N number of steps on a unit lattice with dimension 'dims'"""

    # Re-defining variables for simplicity
    N: int = num_steps

    # creating the formula using a combination of numpy square root and numpy power
    expected_value: NDArray[np.float_] = np.sqrt(2 * N / dims) * np.power(
        gamma((dims + 1) / 2) / gamma(dims / 2), 2
    )
    return expected_value


# Referred to https://pynative.com/python-range-for-float-numbers/
# for a float number of steps using numpy.arange


def plot(ax: Axes) -> None:
    # dimensions within 1 to 25 for all Real Numbers
    dims: NDArray[np.float_] = np.arange(1, 26, dtype=np.float_)

    # Number of Steps
    num_steps: int = 20_000

    # y-axis
    y: NDArray[np.float_] = exp_dist(dims, num_steps)

    # Plotting the Expected distance as a function of dimensions
    # Added some customization to the graphs. Orange line and almost transparent grid
    ax.plot(dims, y, color="orange")
    ax.set_title("Expected Final Distance")
    ax.set_xlabel("Dimensions")
    ax.set_ylabel("Mean Final Distance")

    # adjusting alpha value makes grids more transparent or opaque
    ax.grid(alpha=0.2)
    ax.plot()


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
