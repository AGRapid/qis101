#!/usr/bin/env python3
"""factor_quadratic.py"""

import numpy as np

# Used Biersach's code to complete this task


def factor_quadratic(h: int, i: int, j: int) -> None:
    """Displays factors of the quadratic polynomial Jx^2 + Kx + L"""

    print(f"Given the quadratic:{h}x^2 + {i}x + {j}")
    # inclusive h, where h = J

    # factoring out shared gcd between all coefficients
    g: int = int(np.gcd(h, np.gcd(i, j)))
    h, i, j = h // g, i // g, j // g

    found_factor: bool = False

    # for loop to find factors of the quadratic
    for a in range(1, h + 1):
        if h % a == 0:
            c: int = h // a  # // is making it clear you are doing integer division
            for b in range(1, j + 1):
                if j % b == 0:
                    d: int = j // b
                    # Testing whether it gives you i = K
                    # If true, print the values
                    if int(a * d + b * c) == i:
                        print("The factors are:", end=" ")
                        if g > 0:
                            print(f"({g})", end=" ")
                        print(f"({a}x + {b})({c}x + {d})")
                        found_factor = True
                        break

            if found_factor:
                break

    if not found_factor:
        print("The quadratic cannot be factored because it is prime.")


def main() -> None:
    factor_quadratic(115425, 3254121, 379020)
    factor_quadratic(115425, 3254121, 379021)
    """ Updated numbers to reflect task 04-03 """


if __name__ == "__main__":
    main()
