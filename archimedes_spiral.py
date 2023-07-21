#!/usr/bin/env python3
"""archimedes_spiral.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate  # type: ignore

# Integration from
# https://docs.scipy.org/doc/scipy/tutorial/integrate.html

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def arc_spiral(theta: np.float_) -> NDArray[np.float_]:
    """This function introduces the arc_length function before integration"""
    return np.sqrt(theta**2 + 1)


def plot(ax: Axes) -> None:
    """This function will plot the archimedes spiral"""

    # Theta will be within a domain of 0 <= theta <= 8 pi
    theta: NDArray[np.float_] = np.linspace(0, 8 * np.pi, 1000, dtype=np.float_)

    # Integrating the arc_spiral function
    arc_length, err = scipy.integrate.quad(arc_spiral, 0, 8 * np.pi)

    # referenced David Biersach's code for the plotting

    # Converting polar to cartesian
    x = theta * np.cos(theta)
    y = theta * np.sin(theta)

    # Plotting the Spiral
    ax.set_title(
        (
            r"Archimedes Spiral $(r=\theta, \;0\leq\theta\leq 8\pi)$"
            f"\nArc Length = {arc_length:.4f}"
        )
    )
    ax.plot(x, y)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.axhline(0, color="black")
    ax.axvline(0, color="black")

    # Equal aspect ratio for accurate representation on a computer
    ax.set_aspect("equal")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
