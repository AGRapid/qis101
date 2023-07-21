#!/usr/bin/env python3
"""ifs_hexagonal.py"""

import numpy as np
from ifs import IteratedFunctionSystem
from pygame import Color
from simple_screen import SimpleScreen

# Storing in variable ifs
ifs = IteratedFunctionSystem()

# David's solution


def plot_ifs(ss: SimpleScreen) -> None:
    """This function will plot the fractal pattern"""
    # 200_000 iterations to generate the fractal
    iterations = 200_000
    # initial points
    x: float = 0.0
    y: float = 0.0
    clr: Color

    # Iterate (but don't draw) to let IFS reach its stable orbit
    for _ in range(100):
        x, y, clr = ifs.transform_point(x, y)

    # Now draw each pixel in the stable orbit
    for _ in range(iterations):
        x, y, clr = ifs.transform_point(x, y)
        # set_world_pixel will color each pixel in the x and y coordinate
        ss.set_world_pixel(x, y, clr)


def main() -> None:
    """This function will encode the hexagonal fractal pattern by mapping"""

    # Creates the ifs frame from (0,0) to (30,30) "30x30"
    ifs.set_base_frame(0, 0, 30, 30)

    # equation for height of hexagon
    h = 5 * np.sqrt(3)

    p: float = 1 / 6

    # Encoding each
    # 1. COD
    ifs.add_mapping(25, 15, 15, 15, 20, 15 + h, Color("blue"), p)
    # 2. DOE
    ifs.add_mapping(20, 15 + h, 15, 15, 10, 15 + h, Color("blue"), p)
    # 3. EOF
    ifs.add_mapping(10, 15 + h, 15, 15, 5, 15, Color("blue"), p)
    # 4. FOA
    ifs.add_mapping(5, 15, 15, 15, 10, 15 - h, Color("blue"), p)
    # 5. AOB
    ifs.add_mapping(10, 15 - h, 15, 15, 20, 15 - h, Color("blue"), p)
    # 6. BOC
    ifs.add_mapping(20, 15 - h, 15, 15, 25, 15, Color("blue"), p)

    ifs.generate_transforms()

    ss = SimpleScreen(
        # world_rect sets the window
        world_rect=((0, 0), (30, 30)),
        # setting screen window pixels
        screen_size=(900, 900),
        # calling the plot function to draw after stabilizing
        draw_function=plot_ifs,
        # setting title
        title="IFS Hexagonal",
    )
    # will display the pattern
    ss.show()


if __name__ == "__main__":
    main()
