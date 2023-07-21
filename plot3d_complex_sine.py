#!/usr/bin/env python3
"""plot3d_complex_sine.py"""

from __future__ import annotations


import typing

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

if typing.TYPE_CHECKING:
    from typing import Any
    from matplotlib.axes import Axes

    from numpy.typing import NDArray


def f(z: NDArray[np.float_]) -> NDArray[np.float_]:
    """This defines the complex function absolute value of sine"""
    return np.array(np.abs(np.sin(z)))


def plot(ax: Axes) -> None:
    """Plotting the function and defining the domains"""

    # Making the x axis the real domain
    real_bounds: NDArray[np.float_] = np.linspace(-2.5, 2.5, 1000)
    # Making the y-axis the imaginary domain
    imaginary_bounds: NDArray[np.float_] = np.linspace(-1, 1, 1000)

    # meshgrid is used here to create coordinates from two 1d rays from real and imaginary
    real, imaginary = np.meshgrid(real_bounds, imaginary_bounds)

    # Array of complex floating points stored in z
    z = f(real + 1j * imaginary)

    # Creating the surface plot and changing the colormap to Red and Grey Diverging Colormap
    # Colormaps found https://matplotlib.org/stable/tutorials/colors/colormaps.html
    surface: Any = ax.plot_surface(  # type: ignore
        real, imaginary, z, cmap=cm.RdGy, linewidth=0, antialiased=False  # type: ignore
    )

    # Customizing the plot
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")
    ax.set_zlabel("z")  # type: ignore

    # color bar legend is like a heat value map
    plt.colorbar(surface, ax=ax, shrink=0.5, aspect=5)


def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()


if __name__ == "__main__":
    main()
