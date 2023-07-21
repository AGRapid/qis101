#!/usr/bin/env python3
"""hydrogen_spectrum.py"""

# Appropriated some code from spectrum_rydberg.py and spectrum_bohr.py


def main() -> None:
    """This function calculates and displays the wavelengths of
    both the Pfund and Humphreys high energy spectral series of Hydrogen"""

    # Defining necessary constants
    rydberg_constant: float = 1.0967757e7
    e_charge: float = 1.602e-19
    e_mass: float = 9.109e-31
    permittivity: float = 8.854e-12
    h_plank: float = 6.626e-34
    speed_light: float = 2.998e8

    # Defining Bohr's formula for ground state energy
    e_0: float = (pow(e_charge, 4) * e_mass) / (
        8 * pow(permittivity, 2) * pow(h_plank, 2)
    )

    # Rydberg wavelength formula:

    for k in range(5, 7):  # We want the series transitions for 5 and 6 inclusive
        # Adjusting the position of the lettering to read well.
        print(rf"{'Transition':>16}{'Rydberg Wavelength':>19}")
        for j in range(k + 1, k + 6):
            # Formula for Rydberg waveLength in nanometers
            rydberg_wave_length: float = (
                1 / (rydberg_constant * (1 / pow(k, 2) - 1 / pow(j, 2))) * 1e9
            )
            print(f"\t{j:>2} -> {k:>2}{rydberg_wave_length:8.0f} nm")
        print()

    print()

    # Bohr Wavelength Formula:

    for final_orbit in range(
        5, 7
    ):  # We want the series transitions for 5 and 6 inclusive
        # Adjusting the positions of the lettering to read well.
        print(f"{'Transition':>16}{'Bohr Wavelength':>16}")
        for init_orbit in range(final_orbit + 1, final_orbit + 6):
            # The initial energy levels
            e_i: float = -e_0 / pow(init_orbit, 2)
            # The final energy levels
            e_f: float = -e_0 / pow(final_orbit, 2)
            # Formula for Bohr waveLength in nanometers
            bohr_wave_length: float = h_plank * speed_light / (e_i - e_f) * 1e9
            print(f"\t{init_orbit:>2} -> {final_orbit:>2}{bohr_wave_length:8.0f} nm")
        print()
    # This print() is here to add spacing between the tables
    print()


if __name__ == "__main__":
    main()
