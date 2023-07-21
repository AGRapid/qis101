#!/usr/bin/env python3
"""euler_curve.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

# Referenced David Biersach's Code for the Plot Function


def f_1(t: float) -> float:
    """This defines the function in x(t)"""
    return np.cos(t**2)


def f_2(t: float) -> float:
    """This defines the function in y(t)"""
    return np.sin(t**2)


def f_3(t: float) -> float:
    """This defines the arc length"""
    return np.sqrt(np.cos(t**2) ** 2 + np.sin(t**2) ** 2)


def plot(ax: Axes) -> None:
    """This function will integrate and plot x(t), y(t). It will also compute arc length"""
    # Defining the final t
    tf: float = 12.34
    # Range of t from 0 <= t < tf
    t: NDArray[np.float_] = np.linspace(0, tf, 1000)

    # Arc length is found by integrating f_3 from 0 to tf
    arc_length: float = quad(f_3, 0, tf)[0]  # type: ignore

    # Next  lines obtained from Chat GPT 7/18/2023
    # Initializing arrays to zero with the same amount of indices as t
    x = np.zeros_like(t)
    y = np.zeros_like(t)

    # for loop iterating over each element in t and computes the integral for each
    for i, _ in enumerate(t):
        # calling the first element in the array with [0]
        x[i] = quad(f_1, 0, _)[0]
        y[i] = quad(f_2, 0, _)[0]

    # Plotting x and y after populating the arrays
    ax.plot(x, y)

    # Plot Customization Obtained from Biersach's code.
    ax.set_title((rf"Euler's Curve $(0\leq t<{tf:.2f})$ arc length = {arc_length:.2f}"))
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")

    # Calculating and representing the center of the circle in the plot as a red dot
    c: float = np.sqrt(np.pi / 2) / 2
    ax.scatter(c, c, color="red")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
