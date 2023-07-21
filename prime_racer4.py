#!/usr/bin/env python3
"""prime_racer4 .py"""

from math import sqrt
from random import randint, seed
from time import process_time

# USED Chat GPT TO OPTIMIZE AND HELP ADJUST THE CODE

# To make prime racer faster, instead of finding primes, use Sieve of Eratosthenes algorithm
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes


# Used https://www.geeksforgeeks.org/sieve-of-eratosthenes/ for reference
# as to how to code the algorithm


def SieveOfEratosthenes(n) -> set[int]:
    """This function employs the algorithm to find all prime numbers up to a given limit"""

    prime = [True] * (n + 1)
    # initializing a list as True. Multiplying n+1 ensures the list has enough indices for n

    prime[0] = prime[1] = False
    # initializing first two indices as false because they are not prime

    p = 2  # first prime number is 2

    while p <= sqrt(n):  # Iterate if number <= sqrt(1_000_000)
        if prime[p]:  # checking if the number is prime, if not, iterates again
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1  # next number after p = 2 is computed and so on...

    primes: set[int] = {i for i in range(2, n + 1) if prime[i]}
    # set comprehension iterating from 2 to n inclusive
    return primes


def main() -> None:
    """This function will define our sample range, print, and time the result"""
    seed(2016)  # Ensures the sequence of random numbers will be the same

    # defining values
    num_samples: int = 10_000
    min_val: int = 100_000
    max_val: int = 1_000_000

    print(
        (
            f"Counting the number of primes in {num_samples:,} random samples\n"
            f"with each sample having a value between {min_val:,} "
            f"and {max_val:,} inclusive . . ."
        )
    )

    # using list comprehension to create a list of random integers within our
    # limit values. Will use 10,000 samples of integers to find primes
    samples: list[int] = [randint(min_val, max_val) for _ in range(num_samples)]

    # The primes found using Sieve of Eratosthenes algorithm are stored here
    primes = SieveOfEratosthenes(max_val)
    # we can use max_val directly here because the function will iterate up to "n"

    # timing the function
    start_time: float = process_time()
    num_primes: int = sum(1 for max_val in samples if max_val in primes)
    # if condition checks if the value is a prime
    # generator expression creates a sequence of 1's for each prime value
    # once the 1's are generated, the indices that are prime will be summed
    elapsed_time: float = process_time() - start_time

    print(f"Number of primes found: {num_primes:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")


if __name__ == "__main__":
    main()
