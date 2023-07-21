#!/usr/bin/env python3
"""plot3d_cylinder.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes

    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    """This function will plot the cylinder"""

    # Angle goes from 0 to 2*pi
    v: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 30)

    # The range of z must go from -1 to 1 in order to be centered at zero
    zr: NDArray[np.float_] = np.linspace(-1, 1, 30)

    # Inputting cylindrical coords for x and y values with unit radius, so r = 1
    x: NDArray[np.float_] = np.cos(v)
    y: NDArray[np.float_] = np.sin(v)

    # z must be two dimensional. Can achieve using meshgrid
    v_mesh, z = np.meshgrid(v, zr)  # type: ignore

    # customizing the plot
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")  # type: ignore

    # wireframe and changed color to orange
    ax.plot_wireframe(x, y, z, color="orange")  # type: ignore


def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()


if __name__ == "__main__":
    main()
