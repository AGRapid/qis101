#!/usr/bin/env python3
"""identify_element.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

# Linear Regression pulled from David Biersach's Code for Task 16-02
# which is similar to this problem

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
    """This function will plot and call the .csv data
    containing information about the temperature and volume"""
    data_file: Path = Path(__file__).parent.joinpath("task17-01.csv")
    data: NDArray[np.float_] = np.genfromtxt(data_file, delimiter=",")

    # assigning the values of the columns to an array labeled temperature "t"
    # and volume "v"
    t = data[:, 0] + 273.15  # converting to kelvin from celsius
    v = data[:, 1] / 1000  # converting to m^3

    # Defining the intercept and float as a floating point and tuple
    m: float
    b: float
    # assigns the values from the linear fit onto m and b
    m, b = linear_fit(t, v)

    # Pressure
    p = 2.0 * 101325  # atm to pascal
    # Given mass of gas
    mass = 50  # in grams
    gas_constant = 8.3145  # J/(mol*K)

    # finding the molar mass by finding the moles of the gas
    moles = (m * p) / gas_constant
    molar_mass = mass / moles

    # Plotting a graph of temperature vs volume
    ax.scatter(t, v)
    ax.plot(t, m * t + b, color="red", linewidth=2)

    # Customizing the plot
    ax.set_title(f" Plot of Temperature vs Volume for Argon {molar_mass:.2f}u")
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel(r"$Volume (m^3)$")
    ax.grid()


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
