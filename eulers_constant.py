#!/usr/bin/env python3
"""eulers_constant.py"""

from __future__ import annotations

import typing
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate
from matplotlib.axes import Axes

if typing.TYPE_CHECKING:
    from numpy.typing import NDArray


def euler_f(x: np.float_) -> np.float_:
    """euler_f() defines the function that is to be integrated"""
    return np.float_(np.log(np.log(1 / x)))


# Obtained harmonic number formula from
# https://www.geeksforgeeks.org/program-to-find-the-nth-harmonic-number/
def harmonic(N: int) -> NDArray[np.float_]:
    """This function defines the formula to obtain an array of harmonic numbers up to N"""
    harmonic: NDArray[np.float_] = np.zeros(N, dtype=np.float_)
    harmonic[1] = 1.0
    for i in range(2, N):
        harmonic[i] = harmonic[i - 1] + 1.0 / i
    return harmonic


def plot(ax: Axes) -> None:
    """This function integrates euler_f and creates a superimposed plot of
    a step function of harmonic_nums and a line curve of the asymptotic limit"""

    # Integrating euler_f()
    gamma: np.float_ = -scipy.integrate.quad(euler_f, 0, 1)[0]

    # Defining the domain. Array slicing to exclude zero since log(0) is undefined
    x: NDArray[np.float_] = np.linspace(0, 50, 1_000)[1:]

    # Asymptotic limit formula
    asym_limit: NDArray[np.float_] = gamma + np.log(x)

    # Harmonic Numbers obtained and stored
    harmonic_nums: NDArray[np.float_] = harmonic(50)

    # Creating the Step Plot and line plot for the respective functions
    ax.step(
        np.arange(50),
        harmonic_nums,
        where="mid",
        label=r"Harmonic Numbers: $\sum_{k=1}^n = \frac{1}{k}$",
    )
    # added a -0.5 offset to have the asymptotic limit pass through the midpoints of
    # step function. Maybe something is off
    ax.plot(x - 0.5, asym_limit, label=r"Asymptotic Limit: $\gamma+\ln(x)$")

    # Customizing the plots
    ax.set_title("Step Plot of Harmonic Numbers with Asymptotic Limit")
    ax.set_xlabel("n-values")
    ax.set_ylabel("Harmonic Numbers")
    ax.legend(loc="lower right")
    # adding a grid
    ax.grid(True)

    # setting limits
    ax.set_xlim(0)
    ax.set_ylim(0, 5.5)


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
