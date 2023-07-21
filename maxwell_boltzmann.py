#!/usr/bin/env python3
"""maxwell_boltzmann.py"""

# Calculate and plot the probability density function of the Maxwell
# Boltzmann Distribution

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes

    from numpy.typing import NDArray


def Maxwell_PDF(x: NDArray[np.float_], a: int) -> NDArray[np.float_]:
    """The probability density function formula is obtained from
    https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_distribution"""
    return np.sqrt(2 / np.pi) * (x**2 / a**3) * np.exp(-(x**2 / (2 * a**2)))


# Referred to ChatGPT to help plot the varying a values. DATE: 6/28/2023


def plot(ax: Axes, a: int) -> None:
    """This function will plot the maxwell distribution and introduce the varying parameters"""

    # Limiting the domain on the plot
    x: NDArray[np.float_] = np.linspace(0, 20, 1000, dtype=np.float_)

    # Plotting the domain along the x-axis and the probability on the y-axis
    # formatting with an f string to introduce a legend for the respective a-values
    ax.plot(x, Maxwell_PDF(x, a), label=f"a = {a}")

    ax.set_title("Maxwell Boltzmann Distribution")
    ax.set_xlabel("x-values")
    ax.set_ylabel("Probability")


def main() -> None:
    # Introducing the varying a-values
    a_1 = 1
    a_2 = 2
    a_3 = 5

    # Plot commands
    plt.figure(__file__)
    ax = plt.axes()
    plot(ax, a_1)
    plot(ax, a_2)
    plot(ax, a_3)
    plt.show()


if __name__ == "__main__":
    main()
