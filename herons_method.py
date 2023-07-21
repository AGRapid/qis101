#!/usr/bin/env python3
"""herons_method.py"""

# David Biersach's Code informed this script

from random import randint
from math import sqrt

""" Importing square root to verify results """


def heron_method(s: float) -> float:
    eps = 1e-8
    """ setting epsilon"""
    x: float = s / 2
    """ Variable x is the initial guess for the square root of s"""

    while eps < abs(s - x**2):
        x = (1 / 2) * (s / x + x)
        """ Formula for the revised x value after setting up a while loop"""
    return x


def main() -> None:
    s: int = randint(10**6, 2 * 10**6)
    """ Generating a random integer within 1e+6 to 2e+6 """

    r: float
    r = round(heron_method(s), 8)
    """ Rounding the value of s to 8 decimal places"""
    print(f"The square root of {s:,} using Heron's Method = {r:,f}")

    r_check: float = sqrt(s)
    """ A check to see if the heron method script works"""
    print(f"To verify Heron's method, the square root calculation of s = {r_check:>,f}")


if __name__ == "__main__":
    main()
