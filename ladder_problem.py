#!/usr/bin/env python3
"""ladder_problem.py"""


# Used David Biersach's Solution to the problem

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import numpy as np
import scipy.optimize  # type: ignore

# Optimization
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray
    from scipy.optimize import OptimizeResult  # type: ignore


def length(theta: NDArray[np.float_]) -> NDArray[np.float_]:
    """This function will be used to calculate the length of the ladder.
    The formula originates from the slides"""
    return 2 / np.sin(theta) + 1 / np.cos(theta)


def plot(ax: Axes) -> None:
    """This function will plot and calculate the maximum length og the ladder"""

    # defining the domain of theta. Introducing array slicing by excluding the first
    # value (0) and the last (2pi) because they produce errors in length()
    theta: NDArray[np.float_] = np.linspace(0, np.pi / 2, 1000, dtype=np.float_)[1:-2]

    # Inputting theta domain into the function
    ladder: NDArray[np.float_] = length(theta)

    # Plotting with x-axis as theta and the y-axis as the ladder
    ax.plot(theta, ladder)

    # Scipy optimization function used to find the minimum value of the length function
    # pi/4 is an initial guess for optimization
    res: OptimizeResult = scipy.optimize.minimize(length, np.pi / 4)  # type: ignore

    # Optimized goes into the x array
    c_theta: float = res.x[0]  # type: ignore

    # Optimized theta goes into the length. producing an optimized length
    c_length: float = float(length(np.array(c_theta)))  # type: ignore

    # Customizing the plot
    ax.set_title(f"Max Length = {c_length:.4f} m")
    ax.plot(c_theta, c_length, color="green", marker="o")
    ax.set_xlabel(r"$\theta$ (radians)")
    ax.set_ylabel("length (m)")

    # Adds a horizontal line with a height above the x-axis of c_length
    ax.axhline(c_length, color="gray", linestyle="--")

    # Adds a vertical line from x-axis to c_theta
    ax.vlines(x=c_theta, ymin=0, ymax=c_length, color="red")

    # Adding minor ticks to x and y-axis
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    # limiting the y-axis to only display from 0 to 25
    ax.set_ylim(0, 25)


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
