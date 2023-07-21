#!/usr/bin/env python3
"""hamming_weight.py"""

# Definition from Wikipedia:
# The Hamming weight of a string is the number of symbols that are different
# from the zero-symbol of the alphabet used. It is thus equivalent to the
# Hamming distance from the all-zero string of the same length


def ham_wght(n: int) -> int:
    """This function will convert the integer value into binary and returns an integer"""
    pop_count: int = 0  # initializing the population count

    while n > 0:
        pop_count = n % 2 + pop_count
        # calculates the remainder of the value and accumulates
        n //= 2  # divides and shifts the binary to the right by one
    return pop_count


def main() -> None:
    value: int = 95_601

    print(f"The population count of {value} is {ham_wght(value)}")

    # Comparing with a built-in hamming weight function from
    # https://stackoverflow.com/questions/15233121/calculating-hamming-weight-in-o1#:~:text=In%20binary%20representation%2C%20hamming%20weight%20is%20the%20number%20of%201's.
    pop_count2: int = bin(value).count("1")

    print(f" The Python built-in population count for {value} is {pop_count2}")


if __name__ == "__main__":
    main()

# chat gpt assistance for the binary conversion function
