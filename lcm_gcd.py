#!/usr/bin/env python3
"""lcm_gcd.py"""

from math import gcd

"""Write a Python Program to calculate the lowest common multiple of two integers"""
# NO LOOPING calc and display the LCM of 447618 and 2011835


def main() -> None:
    a: int = 447618
    b: int = 2011835
    """ Assigning the values to variables """
    lcm: float = (a * b) / gcd(a, b)
    """ Formula of LCM """
    print(f"The LCM of 447618 and 2011835 = {lcm:>,.0f}")


if __name__ == "__main__":
    main()
