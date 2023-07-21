#!/usr/bin/env python3
"""sum_multiples.py"""

# I will be using this as an opportunity to play around and get familiar with lists


def main() -> None:
    # Creating a list to store natural numbers divisible by 7 and 11 separately
    nat_num_7: list[int] = []
    nat_num_11: list[int] = []

    # Creating two separate lists two observe and distinguish divisibles
    nat_num_list: list[list[int]] = [nat_num_7, nat_num_11]

    # This will store all the natural numbers divisible by 7 and 11 together
    total_num: list[int] = []

    # Start = 1 for natural numbers, Stop exclusive for <1900
    for n in range(1, 1_900):
        if n % 7 == 0:
            nat_num_7.append(n)  # storing numbers into two lists for the purposes above
            total_num.append(n)
    for m in range(1, 1_900):
        if m % 11 == 0:
            nat_num_11.append(m)  # same as comment above
            total_num.append(m)

    # This gives the sum total of all natural numbers divisible by 7 and 11
    nat_sum: int = sum(total_num)

    # List of lists to distinguish natural numbers (not necessary can remove)
    print(f"Numbers divisible by 7 and 11, respectively: {nat_num_list}")

    # This is what the Task is asking for...
    print(f"The sum of natural numbers divisible by 7 and 11: {nat_sum}")


if __name__ == "__main__":
    main()

# Used https://flexiple.com/python/list-of-lists-python/ as a source for list
