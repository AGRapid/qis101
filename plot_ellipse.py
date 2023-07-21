#!/usr/bin/env python3
"""plot_ellipse.py"""

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from numpy.typing import NDArray


def ellipse_plot(ax) -> None:  # type: ignore
    """This function creates a plot of the ellipse as a function of theta, radius,
    major, and minor axis"""

    # Major Axis
    a = 100

    # Minor Axis
    b = 50

    # First is to calculate the points on the perimeter of the ellipse using polar

    # Sweeping theta through an interval of 0 to 2 pi with steps of 1000
    theta: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 1000)

    # Radius as a function of theta in polar coords
    radius = (a * b) / np.sqrt((b * np.cos(theta)) ** 2 + (a * np.sin(theta)) ** 2)

    # Converting theta and radius into cartesian coords
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # Creating a line plot
    ax.plot(x, y)
    ax.set_title(rf"$(\frac{{x}}{{{a}}})^2 + (\frac{{y}}{{{b}}})^2= 1$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid()
    ax.axhline(0, color="black")
    ax.axvline(0, color="black")

    # Adjusting the aspect ratio to be representative of the actual plot
    ax.set_aspect("equal")


def main() -> None:
    """This function displays the figure"""
    plt.figure("Ellipse Plot")
    ellipse_plot(plt.axes())
    # need plt.show to make the window appear
    plt.show()


if __name__ == "__main__":
    main()
