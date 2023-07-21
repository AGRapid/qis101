#!/usr/bin/env python3
"""plot_trajectory.py"""


# Used David's Code for the Solution

from __future__ import annotations

import typing

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def linear_fit(x: NDArray[np.float_], y: NDArray[np.float_]) -> tuple[float, float]:
    """This function will define the fit of a linear regression line onto values of x and y"""

    # Calculating the length of the x-array
    n: int = len(x)
    # Calculating the slope of the linear regression line
    m: float = float(n * np.sum(x * y) - np.sum(x) * np.sum(y))
    m /= float(n * np.sum(x**2) - np.sum(x) ** 2)
    # Calculating the intercept
    b: float = float(np.sum(y) - m * np.sum(x))
    # dividing intercept by number of data points
    b /= n
    return m, b


def plot(ax: Axes) -> None:
    """This function will lot and call the .csv data"""
    data_file: Path = Path(__file__).parent.joinpath("ray.csv")
    data = np.genfromtxt(data_file, delimiter=",")  # type: ignore

    # assigning the values of the columns to an array labeled x and y
    x = data[:, 0]
    y = data[:, 1]

    # Defining the intercept and float as a floating point and tuple
    m: float
    b: float
    # assigns the values from the linear fit onto m and b
    m, b = linear_fit(x, y)
    # Calculating the height
    h = (np.abs(m) * 1e9 / 100) * (0.1743 / 1e30) / 1000
    # speed of light in cm/ns
    c = 29.98

    # Printing the unknown variables.
    # Specifying format options where :.4f means 4 decimal places
    # and :,.2f means separating thousands with a comma and two decimal places
    print(f"Slope = {abs(m):.4f} cm/ns")
    print(f"Velocity = {np.abs(m)/c:,.2f} c")
    # printing the height
    print(f"Height = {h:,.2f} km")

    # plotting the finction
    ax.scatter(x, y)
    ax.plot(x, m * x + b, color="red", linewidth=2)

    # Customizing the plot
    ax.set_title("Secondary Cosmic Ray Trajectory")
    ax.set_xlabel("Time (ns)")
    ax.set_ylabel("Height (cm)")
    ax.grid()


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
