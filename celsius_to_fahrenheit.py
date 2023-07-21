#!/usr/bin/env python3
"""celsius_to_fahrenheit.py"""

# Converting temperature from Celsius to Fahrenheit


def main() -> None:
    # Start= -44, Stop is 107 for 106 inclusive, steps = 4
    for fahrenheit in range(-44, 107, 4):
        celsius: float = (fahrenheit - 32) * 5 / 9
        # Format Specifier >6.2. ">" Right aligned, "6" width of output, ".2" dps
        print(f"{fahrenheit:>6.2f} F = {celsius:>6.2f} C ")


if __name__ == "__main__":
    main()
