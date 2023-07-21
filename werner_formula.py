""" werner_formula.py """

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


def f_1(x: np.float_) -> np.float_:
    """Defining first sine function"""
    a: np.float_ = 0.8 * x
    return np.sin(a)


def f_2(x: np.float_) -> np.float_:
    """Defining second sine function"""
    b: np.float_ = 0.5 * x
    return np.sin(b)


def f_3(x: np.float_) -> np.float_:
    """Defining the product of both sine functions"""
    return f_1(x) * f_2(x)


# Werner formula obtained from
# https://mathworld.wolfram.com/WernerFormulas.html
def f_4(x: np.float_) -> np.float_:
    """Werner's Product-to-sum formula for the sine product"""
    a: np.float_ = 0.8 * x
    b: np.float_ = 0.5 * x
    return (np.cos(a - b) - np.cos(a + b)) / 2


def plot(ax: Axes) -> None:
    """This plots all functions on the same graph"""

    # Defining the domain of x
    x = np.linspace(-3 * np.pi, 3 * np.pi, 1000, dtype=np.float_)  # type: ignore

    # Plotting each function
    ax.plot(x, f_1(x), label="$f_1(x)=sin(0.8x)$")
    ax.plot(x, f_2(x), label="$f_2(x)=sin(0.5x)$")
    ax.plot(x, f_3(x), label="$f_3(x)=sin(0.8x)sin(0.5x)$")
    # linestyle sets a dashed line.
    # marker sets circles with fillstyle making the circles open
    # markevery set to 10 so that f_3 can be seen below f_4.
    ax.plot(
        x,
        f_4(x),
        label="$f_4(x)= (cos(0.3x)-cos(1.3x))/2$",
        linestyle="--",
        marker="o",
        fillstyle="none",
        markevery=10,
    )

    # Customizing the plot
    ax.set_title("Werner Formula")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="lower center")
    ax.grid(True)


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
